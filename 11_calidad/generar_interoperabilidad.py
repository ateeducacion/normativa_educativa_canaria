#!/usr/bin/env python3
"""Generate public semantic exports from canonical normative frontmatter."""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys
from typing import Any

import yaml


ROOT = pathlib.Path(__file__).resolve().parent.parent
PUBLIC_BASE = "https://ateeducacion.github.io/normativa_educativa_canaria/"
SCHEMA_CONTEXT = "https://schema.org/"
START_MARKER = "<!-- datos-estructurados:inicio -->"
END_MARKER = "<!-- datos-estructurados:fin -->"
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)
LEGISLATION_PATH = ROOT / "docs" / "datos" / "legislacion.jsonld"
CATALOG_PATH = ROOT / "docs" / "datos" / "catalogo.jsonld"
AKN_PATH = ROOT / "docs" / "datos" / "akoma-ntoso" / "NOR-004-articulo-1.xml"
INDEX_HTML = ROOT / "docs" / "index.html"

ARTICLE_1_PARAGRAPHS = (
    "La presente ley tiene por objeto regular el sistema educativo canario y su "
    "evaluación, de modo que pueda convertirse en un instrumento eficaz para hacer "
    "efectivo el derecho a una educación de calidad, inclusiva e integradora, que "
    "garantice la equidad y la excelencia, la prestación de un servicio público "
    "esencial y convertirse, a la vez, en uno de los motores del desarrollo social, "
    "económico y cultural del archipiélago.",
    "El ámbito de aplicación de la presente ley es todo el sistema educativo canario, "
    "a excepción del universitario, en consonancia con las competencias asumidas en "
    "el Estatuto de Autonomía de Canarias y en el desarrollo de las normas básicas "
    "aprobadas por el Estado.",
)


def normalize(value: Any) -> Any:
    """Convert PyYAML dates to the JSON-compatible ISO representation."""
    if isinstance(value, (datetime.datetime, datetime.date)):
        return value.isoformat()
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize(item) for item in value]
    return value


def load_norms() -> list[tuple[pathlib.Path, dict[str, Any]]]:
    """Load normative frontmatter and retain its canonical repository path."""
    norms = []
    for path in sorted(ROOT.glob("02_normativa/**/NOR-*.md")):
        match = FRONTMATTER.match(path.read_text(encoding="utf-8"))
        if match is None:
            raise ValueError(f"{path.relative_to(ROOT)} no contiene frontmatter YAML")
        data = normalize(yaml.safe_load(match.group(1)))
        if not isinstance(data, dict):
            raise ValueError(f"{path.relative_to(ROOT)} no contiene un objeto YAML")
        norms.append((path, data))
    return norms


def public_url(path: pathlib.Path) -> str:
    """Return a stable GitHub Pages URL for a repository path."""
    return PUBLIC_BASE + path.relative_to(ROOT).as_posix()


def legislation_ref(identifier: str, paths_by_id: dict[str, pathlib.Path]) -> dict[str, str]:
    """Build an internal semantic reference without inventing an official URI."""
    path = paths_by_id.get(identifier)
    if path is None:
        raise ValueError(f"La relación apunta a una norma inexistente: {identifier}")
    return {"@id": public_url(path), "@type": "Legislation"}


def legal_force(status: str) -> str | None:
    """Map the controlled status prefix to Schema.org legal-force terms."""
    if status.startswith(("Derogada parcialmente", "Parcialmente vigente")):
        return "https://schema.org/PartiallyInForce"
    if status.startswith(("Derogada", "Superada", "Sustituida", "Histórica")):
        return "https://schema.org/NotInForce"
    if status.startswith("Vigente"):
        return "https://schema.org/InForce"
    return None


def build_legislation() -> dict[str, Any]:
    """Build a Schema.org Legislation graph for every canonical normative record."""
    norms = load_norms()
    paths_by_id = {data["id"]: path for path, data in norms}
    graph = []

    for path, data in norms:
        identifiers: list[Any] = [
            {
                "@type": "PropertyValue",
                "propertyID": "identificador interno",
                "value": data["id"],
            }
        ]
        if data.get("uri_eli"):
            identifiers.append(
                {
                    "@type": "PropertyValue",
                    "propertyID": "ELI",
                    "value": data["uri_eli"],
                }
            )

        item: dict[str, Any] = {
            "@id": public_url(path),
            "@type": "Legislation",
            "name": data["titulo"],
            "alternateName": data["nombre_corto"],
            "identifier": identifiers,
            "legislationIdentifier": [data["id"]]
            + ([data["uri_eli"]] if data.get("uri_eli") else []),
            "legislationType": data["tipo_norma"],
            "legislationJurisdiction": {
                "@type": "AdministrativeArea",
                "name": "Comunidad Autónoma de Canarias"
                if data["ambito"] == "canarias"
                else data["ambito"],
            },
            "legislationPassedBy": {
                "@type": "Organization",
                "name": data["autoridad"],
            },
            "inLanguage": "es",
            "url": public_url(path),
            "sameAs": list(
                dict.fromkeys(
                    [data["url_oficial"]]
                    + ([data["uri_eli"]] if data.get("uri_eli") else [])
                )
            ),
        }

        for source, target in (
            ("fecha_disposicion", "legislationDate"),
            ("fecha_publicacion", "datePublished"),
        ):
            if data.get(source):
                item[target] = data[source]
        if data.get("temas"):
            item["keywords"] = data["temas"]
        force = legal_force(data["estado_vigencia"])
        if force:
            item["legislationLegalForce"] = {"@id": force}

        relations = data.get("relaciones") or {}
        for source, target in (
            ("modifica_a", "legislationAmends"),
            ("deroga_a", "legislationRepeals"),
        ):
            references = [
                legislation_ref(identifier, paths_by_id)
                for identifier in relations.get(source, [])
                if identifier.startswith("NOR-")
            ]
            if references:
                item[target] = references
        graph.append(item)

    return {"@context": SCHEMA_CONTEXT, "@graph": graph}


def build_catalog(legislation: dict[str, Any]) -> dict[str, Any]:
    """Describe the public corpus as a Schema.org Dataset for discovery clients."""
    dates = [
        item.get("datePublished")
        for item in legislation["@graph"]
        if item.get("datePublished")
    ]
    distributions = [
        ("Inventario del corpus", "datos/inventario.json", "application/json"),
        ("Metadatos de legislación", "datos/legislacion.jsonld", "application/ld+json"),
        ("Índice normativo", "06_indices/normativa.yaml", "application/yaml"),
        ("Guía para modelos de lenguaje", "llms.txt", "text/plain"),
        (
            "Piloto Akoma Ntoso",
            "datos/akoma-ntoso/NOR-004-articulo-1.xml",
            "application/akn+xml",
        ),
    ]
    dataset: dict[str, Any] = {
        "@context": SCHEMA_CONTEXT,
        "@id": PUBLIC_BASE + "#dataset",
        "@type": "Dataset",
        "name": "Normativa Educativa Canaria",
        "description": (
            "Corpus abierto y versionado de normativa y currículos educativos de "
            "Canarias, con fuentes oficiales, relaciones y metadatos para reutilización."
        ),
        "url": PUBLIC_BASE,
        "inLanguage": "es",
        "isAccessibleForFree": True,
        "license": "https://creativecommons.org/publicdomain/zero/1.0/",
        "creator": {
            "@type": "Organization",
            "name": "Área de Tecnología Educativa",
        },
        "publisher": {
            "@type": "Organization",
            "name": "Área de Tecnología Educativa",
        },
        "keywords": [
            "normativa educativa",
            "Canarias",
            "currículo",
            "datos jurídicos",
            "educación",
        ],
        "includedInDataCatalog": {
            "@type": "DataCatalog",
            "name": "Catálogo público del corpus",
            "url": PUBLIC_BASE + "datos/catalogo.jsonld",
        },
        "distribution": [
            {
                "@type": "DataDownload",
                "name": name,
                "contentUrl": PUBLIC_BASE + path,
                "encodingFormat": media_type,
            }
            for name, path, media_type in distributions
        ],
    }
    if dates:
        dataset["temporalCoverage"] = f"{min(dates)}/{max(dates)}"
    return dataset


def render_akoma_ntoso() -> str:
    """Render the reviewed Article 1 pilot as an Akoma Ntoso 3.0 portion."""
    first, second = ARTICLE_1_PARAGRAPHS
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <portion includedIn="/akn/es-cn/act/2014-07-25/6">
    <meta>
      <identification source="#corpus">
        <FRBRWork>
          <FRBRthis value="/akn/es-cn/act/2014-07-25/6/!art_1"/>
          <FRBRuri value="/akn/es-cn/act/2014-07-25/6"/>
          <FRBRalias name="ELI" value="https://www.boe.es/eli/es-cn/l/2014/07/25/6/con"/>
          <FRBRdate date="2014-07-25" name="Generation"/>
          <FRBRauthor href="#parlamento-canarias"/>
          <FRBRcountry value="es-cn"/>
          <FRBRnumber value="6"/>
          <FRBRname value="Ley"/>
        </FRBRWork>
        <FRBRExpression>
          <FRBRthis value="/akn/es-cn/act/2014-07-25/6/spa@/!art_1"/>
          <FRBRuri value="/akn/es-cn/act/2014-07-25/6/spa@"/>
          <FRBRdate date="2014-08-07" name="Publication"/>
          <FRBRauthor href="#parlamento-canarias"/>
          <FRBRlanguage language="spa"/>
        </FRBRExpression>
        <FRBRManifestation>
          <FRBRthis value="/akn/es-cn/act/2014-07-25/6/spa@/xml/!art_1"/>
          <FRBRuri value="/akn/es-cn/act/2014-07-25/6/spa@/xml"/>
          <FRBRdate date="2026-08-22" name="Generation"/>
          <FRBRauthor href="#corpus"/>
        </FRBRManifestation>
      </identification>
      <references source="#corpus">
        <TLCOrganization eId="parlamento-canarias" href="https://www.parcan.es/" showAs="Parlamento de Canarias"/>
        <TLCOrganization eId="corpus" href="https://github.com/ateeducacion/normativa_educativa_canaria" showAs="Normativa Educativa Canaria"/>
      </references>
    </meta>
    <portionBody>
      <article eId="art_1">
        <num>Artículo 1.</num>
        <heading>Objeto y ámbito.</heading>
        <paragraph eId="art_1__para_1">
          <num>1.</num>
          <content><p>{first}</p></content>
        </paragraph>
        <paragraph eId="art_1__para_2">
          <num>2.</num>
          <content><p>{second}</p></content>
        </paragraph>
      </article>
    </portionBody>
  </portion>
</akomaNtoso>
'''


def replace_html_block(text: str, dataset: dict[str, Any]) -> str:
    """Replace the single generated JSON-LD block in the public home page."""
    if text.count(START_MARKER) != 1 or text.count(END_MARKER) != 1:
        raise ValueError("docs/index.html debe contener un único bloque de datos estructurados")
    script = "\n".join(
        [
            START_MARKER,
            '    <script type="application/ld+json">',
            json.dumps(dataset, ensure_ascii=False, indent=2, sort_keys=True),
            "    </script>",
            f"    {END_MARKER}",
        ]
    )
    before, remainder = text.split(START_MARKER, 1)
    _, after = remainder.split(END_MARKER, 1)
    return f"{before}{script}{after}"


def expected_files() -> dict[pathlib.Path, str]:
    """Return all generated semantic exports and their expected content."""
    legislation = build_legislation()
    catalog = build_catalog(legislation)
    json_options = {"ensure_ascii": False, "indent": 2, "sort_keys": True}
    return {
        LEGISLATION_PATH: json.dumps(legislation, **json_options) + "\n",
        CATALOG_PATH: json.dumps(catalog, **json_options) + "\n",
        AKN_PATH: render_akoma_ntoso(),
        INDEX_HTML: replace_html_block(INDEX_HTML.read_text(encoding="utf-8"), catalog),
    }


def write_files(files: dict[pathlib.Path, str]) -> None:
    """Write generated files, creating output directories when needed."""
    for path, content in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"Actualizado: {path.relative_to(ROOT)}")


def check_files(files: dict[pathlib.Path, str]) -> int:
    """Fail if a generated semantic output is missing or stale."""
    stale = [
        path.relative_to(ROOT)
        for path, expected in files.items()
        if not path.exists() or path.read_text(encoding="utf-8") != expected
    ]
    if not stale:
        print("Exportaciones interoperables actualizadas.")
        return 0
    print("Exportaciones interoperables desactualizadas:", file=sys.stderr)
    for path in stale:
        print(f"- {path}", file=sys.stderr)
    print(
        "Ejecute: python3 11_calidad/generar_interoperabilidad.py --write",
        file=sys.stderr,
    )
    return 1


def main() -> int:
    """Generate or check the public semantic export layer."""
    parser = argparse.ArgumentParser(
        description="Genera metadatos JSON-LD y el piloto Akoma Ntoso."
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Actualiza los archivos.")
    mode.add_argument("--check", action="store_true", help="Comprueba sin escribir.")
    args = parser.parse_args()
    files = expected_files()
    if args.write:
        write_files(files)
        return 0
    return check_files(files)


if __name__ == "__main__":
    raise SystemExit(main())
