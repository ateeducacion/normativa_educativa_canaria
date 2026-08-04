#!/usr/bin/env python3
"""Valida el corpus contra los esquemas de `schemas/` y contra sus índices YAML.

Comprueba tres cosas que hasta ahora no comprobaba nadie:

1. Cada ficha cumple el esquema JSON Schema de su tipo de entidad.
2. El ID del frontmatter coincide con el nombre del fichero.
3. Cada entidad está registrada en su índice de `06_indices/` y cada entrada
   del índice apunta a una entidad que existe (regla R11 de AGENTS.md).

Uso:

    python3 11_calidad/validar_corpus.py              # informe legible
    python3 11_calidad/validar_corpus.py --json       # salida para CI
    python3 11_calidad/validar_corpus.py --tipo NOR   # solo un tipo

Devuelve 1 si hay errores. Los avisos no hacen fallar la ejecución: señalan
campos recomendados ausentes que exigen decisión editorial o evidencia nueva,
y no pueden rellenarse inventando datos (R1).

Dependencias: pyyaml, jsonschema.
"""

from __future__ import annotations

import argparse
import datetime
import json
import pathlib
import re
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - guía de instalación
    sys.exit(f"Falta una dependencia ({exc.name}). Instala con: pip install pyyaml jsonschema")

RAIZ = pathlib.Path(__file__).resolve().parent.parent

# tipo -> configuración de validación
#   patron:        glob de las fichas, relativo a la raíz del repositorio
#   esquema:       fichero de `schemas/`
#   origen:        "frontmatter" (YAML entre --- de un .md) o "documento" (.yaml entero)
#   indice:        índice canónico de `06_indices/`
#   recomendados:  campos no obligatorios cuya ausencia se avisa
ENTIDADES = {
    "FTE": {
        "patron": "01_fuentes/**/FTE-*.md",
        "esquema": "fuente.schema.yaml",
        "origen": "frontmatter",
        "indice": "fuentes.yaml",
        "recomendados": ["fecha_analisis", "nivel_evidencia", "relacionadas"],
    },
    "NOR": {
        "patron": "02_normativa/**/NOR-*.md",
        "esquema": "norma.schema.yaml",
        "origen": "frontmatter",
        "indice": "normativa.yaml",
        "recomendados": ["temas"],
    },
    "CUR": {
        "patron": "03_curriculos/**/CUR-*.yaml",
        "esquema": "curriculum.schema.yaml",
        "origen": "documento",
        "indice": "curriculos.yaml",
        "recomendados": [],
    },
    "REL": {
        "patron": "05_relaciones/**/REL-*.yaml",
        "esquema": "relacion.schema.yaml",
        "origen": "documento",
        "indice": "relaciones.yaml",
        "recomendados": [],
    },
    "PREG": {
        "patron": "08_tareas/preguntas/PREG-*.md",
        "esquema": "pregunta.schema.yaml",
        "origen": "frontmatter",
        "indice": "preguntas.yaml",
        "recomendados": [],
    },
    "TAREA": {
        "patron": "08_tareas/backlog/TAREA-*.md",
        "esquema": "tarea.schema.yaml",
        "origen": "frontmatter",
        "indice": "tareas.yaml",
        "recomendados": [],
    },
}

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---", re.S)
ID_EN_NOMBRE = re.compile(r"\A([A-Z]+-[0-9]+)")


def normalizar(valor):
    """Convierte fechas de PyYAML a cadenas ISO.

    `fecha_consulta: 2026-04-26` sin comillas es un `datetime.date` para YAML,
    pero los esquemas declaran `type: string`. Normalizar aquí evita tener que
    entrecomillar cientos de fechas o relajar el tipo del esquema.
    """
    if isinstance(valor, (datetime.datetime, datetime.date)):
        return valor.isoformat()
    if isinstance(valor, dict):
        return {k: normalizar(v) for k, v in valor.items()}
    if isinstance(valor, list):
        return [normalizar(v) for v in valor]
    return valor


def cargar(ruta: pathlib.Path, origen: str):
    """Devuelve (datos, error). `datos` es None si no se pudo leer."""
    texto = ruta.read_text(encoding="utf-8")
    if origen == "frontmatter":
        encontrado = FRONTMATTER.match(texto)
        if not encontrado:
            return None, "sin frontmatter YAML delimitado por ---"
        texto = encontrado.group(1)
    try:
        return normalizar(yaml.safe_load(texto)), None
    except yaml.YAMLError as exc:
        return None, f"YAML no parseable: {str(exc).splitlines()[0]}"


def ids_del_indice(nombre: str) -> set[str]:
    ruta = RAIZ / "06_indices" / nombre
    if not ruta.exists():
        return set()
    datos = yaml.safe_load(ruta.read_text(encoding="utf-8")) or {}
    return set(datos) if isinstance(datos, dict) else set()


def validar_tipo(tipo: str, cfg: dict) -> dict:
    esquema_ruta = RAIZ / "schemas" / cfg["esquema"]
    validador = Draft202012Validator(yaml.safe_load(esquema_ruta.read_text(encoding="utf-8")))

    errores: list[dict] = []
    avisos: list[dict] = []
    vistos: set[str] = set()
    ficheros = sorted(RAIZ.glob(cfg["patron"]))

    for fichero in ficheros:
        rel = fichero.relative_to(RAIZ).as_posix()
        datos, fallo = cargar(fichero, cfg["origen"])
        if fallo:
            errores.append({"fichero": rel, "campo": "(fichero)", "mensaje": fallo})
            continue
        if not isinstance(datos, dict):
            errores.append({"fichero": rel, "campo": "(fichero)", "mensaje": "el contenido no es un mapa YAML"})
            continue

        # El ID del frontmatter debe coincidir con el del nombre del fichero (R10).
        en_nombre = ID_EN_NOMBRE.match(fichero.name)
        if en_nombre and datos.get("id") != en_nombre.group(1):
            errores.append({
                "fichero": rel,
                "campo": "id",
                "mensaje": f"el id {datos.get('id')!r} no coincide con el nombre del fichero ({en_nombre.group(1)})",
            })
        if isinstance(datos.get("id"), str):
            vistos.add(datos["id"])

        for error in sorted(validador.iter_errors(datos), key=lambda e: list(e.path)):
            errores.append({
                "fichero": rel,
                "campo": ".".join(str(p) for p in error.path) or "(raíz)",
                "mensaje": error.message,
            })

        for campo in cfg["recomendados"]:
            if campo not in datos or datos[campo] in (None, [], ""):
                avisos.append({"fichero": rel, "campo": campo, "mensaje": "campo recomendado ausente o vacío"})

    # Cobertura de índice (R11). Una ficha fuera del índice es un error: rompe la
    # puerta de entrada del repositorio y siempre se puede corregir. Una entrada de
    # índice sin ficha es deuda documental histórica, que sólo se resuelve
    # reconstruyendo lo que se hizo: se avisa, no se bloquea.
    indexados = ids_del_indice(cfg["indice"])
    for identificador in sorted(vistos - indexados):
        errores.append({
            "fichero": f"06_indices/{cfg['indice']}",
            "campo": identificador,
            "mensaje": f"{identificador} existe como ficha pero no está en el índice",
        })
    for identificador in sorted(indexados - vistos):
        avisos.append({
            "fichero": f"06_indices/{cfg['indice']}",
            "campo": identificador,
            "mensaje": f"{identificador} está en el índice pero no tiene ficha",
        })

    return {
        "tipo": tipo,
        "ficheros": len(ficheros),
        "errores": errores,
        "avisos": avisos,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida el corpus contra schemas/ y 06_indices/.")
    parser.add_argument("--json", action="store_true", help="salida JSON para integración continua")
    parser.add_argument("--tipo", choices=sorted(ENTIDADES), help="validar solo un tipo de entidad")
    parser.add_argument("--sin-avisos", action="store_true", help="omitir los avisos del informe")
    args = parser.parse_args()

    tipos = [args.tipo] if args.tipo else sorted(ENTIDADES)
    informes = [validar_tipo(t, ENTIDADES[t]) for t in tipos]
    total_errores = sum(len(i["errores"]) for i in informes)
    total_avisos = sum(len(i["avisos"]) for i in informes)

    if args.json:
        print(json.dumps({"informes": informes, "errores": total_errores, "avisos": total_avisos},
                         ensure_ascii=False, indent=2))
        return 1 if total_errores else 0

    for informe in informes:
        estado = "OK" if not informe["errores"] else f"{len(informe['errores'])} errores"
        print(f"\n## {informe['tipo']} — {informe['ficheros']} fichas · {estado}")
        for error in informe["errores"]:
            print(f"   ✗ {error['fichero']} [{error['campo']}] {error['mensaje']}")
        if not args.sin_avisos:
            for aviso in informe["avisos"]:
                print(f"   · {aviso['fichero']} [{aviso['campo']}] {aviso['mensaje']}")

    print(f"\n{'—' * 60}")
    print(f"Total: {total_errores} errores · {total_avisos} avisos")
    if total_errores:
        print("Los errores bloquean el cierre de tarea (AGENTS.md §15).")
    return 1 if total_errores else 0


if __name__ == "__main__":
    raise SystemExit(main())
