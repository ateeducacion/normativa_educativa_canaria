document.addEventListener('DOMContentLoaded', () => {
  const catalog = [
    { group: 'Índices', kind: 'yaml', title: 'Índice de normativa', path: '06_indices/normativa.yaml', note: 'Puerta principal para NOR y relaciones de vigencia.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de fuentes', path: '06_indices/fuentes.yaml', note: 'Mapa de fuentes oficiales y portales.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de currículos', path: '06_indices/curriculos.yaml', note: 'Inventario de currículos por etapa y materia.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de relaciones', path: '06_indices/relaciones.yaml', note: 'Relaciones trazables entre normas y currículos.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de chunks', path: '06_indices/chunks.yaml', note: 'Corpus IA breve y autocontenido.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de preguntas', path: '06_indices/preguntas.yaml', note: 'Dudas abiertas y seguimiento editorial.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de tareas', path: '06_indices/tareas.yaml', note: 'Estado del trabajo y coordinación.' },
    { group: 'Índices', kind: 'yaml', title: 'Índice de análisis', path: '06_indices/analisis.yaml', note: 'Notas y comparativas metodológicas.' },
    { group: 'Normativa', kind: 'md', title: 'LOE consolidada', path: '01_fuentes/boe/FTE-005-loe-texto-consolidado.md', note: 'Fuente oficial de referencia del marco básico.' },
    { group: 'Normativa', kind: 'md', title: 'LOMLOE', path: '01_fuentes/boe/FTE-006-lomloe.md', note: 'Ley orgánica modificadora de la LOE.' },
    { group: 'Normativa', kind: 'md', title: 'RD 217/2022', path: '01_fuentes/boe/FTE-007-rd-217-2022.md', note: 'Enseñanzas mínimas de ESO.' },
    { group: 'Normativa', kind: 'md', title: 'Ley Canaria 6/2014', path: '01_fuentes/boe/FTE-008-ley-canaria-6-2014.md', note: 'Ley autonómica de educación.' },
    { group: 'Currículos', kind: 'md', title: 'Biología y Geología ESO', path: '03_curriculos/eso/materias/CUR-001-biologia-y-geologia.md', note: 'Ejemplo de ficha curricular con extracción estructurada.' },
    { group: 'Currículos', kind: 'yaml', title: 'Matemáticas ESO', path: '03_curriculos/eso/materias/CUR-019-matematicas.yaml', note: 'Versión YAML de una ficha curricular.' },
    { group: 'Currículos', kind: 'md', title: 'Conocimiento del Medio', path: '03_curriculos/primaria/materias/CUR-024-conocimiento-medio.md', note: 'Currículo de Primaria.' },
    { group: 'Relaciones', kind: 'yaml', title: 'LOMLOE modifica la LOE', path: '05_relaciones/normativa/REL-001-lomloe-modifica-loe.yaml', note: 'Relación normativa básica.' },
    { group: 'Relaciones', kind: 'yaml', title: 'RD 243/2022 desarrolla LOE/LOMLOE', path: '05_relaciones/normativa/REL-006-rd-243-2022-desarrolla-loe-lomloe.yaml', note: 'Relación estatal de Bachillerato.' },
    { group: 'Relaciones', kind: 'yaml', title: 'ROC CIFP y LOFP', path: '05_relaciones/normativa/REL-039-roc-cifp-relaciona-lofp.yaml', note: 'Relación de FP.' },
    { group: 'Corpus IA', kind: 'yaml', title: 'Chunk LOE: objeto general', path: '07_corpus_ia/chunks/CHUNK-00001-loe-objeto-general.yaml', note: 'Chunk breve preparado para contexto IA.' },
    { group: 'Corpus IA', kind: 'yaml', title: 'Chunk currículo ESO/Bach', path: '07_corpus_ia/chunks/CHUNK-00007-curriculo-eso-bach-resumen.yaml', note: 'Resumen reutilizable.' },
    { group: 'Corpus IA', kind: 'md', title: 'Resumen NOR-001', path: '07_corpus_ia/resumenes/resumen-NOR-001-loe.md', note: 'Resumen IA-friendly de una norma.' },
    { group: 'Docs', kind: 'html', title: 'Home pública', path: 'docs/index.html', note: 'Panel principal del corpus.' },
    { group: 'Docs', kind: 'html', title: 'Skill', path: 'docs/skill.html', note: 'Skill copiable para asistentes.' },
    { group: 'Docs', kind: 'html', title: 'MCP', path: 'docs/mcp.html', note: 'Guía de conexión con GitHub MCP.' },
    { group: 'Docs', kind: 'css', title: 'Estilos del sitio', path: 'docs/assets/css/site.css', note: 'Base visual compartida.' },
    { group: 'Docs', kind: 'js', title: 'Script principal', path: 'docs/assets/js/site.js', note: 'Filtro de tarjetas de la home.' },
    { group: 'Raíz', kind: 'md', title: 'README principal', path: 'README.md', note: 'Introducción y accesos principales.' },
    { group: 'Raíz', kind: 'md', title: 'Índice general', path: 'index.md', note: 'Accesos principales del corpus.' },
    { group: 'Raíz', kind: 'yaml', title: 'Estado del repositorio', path: 'status.yaml', note: 'Seguimiento de tareas y estado.' },
    { group: 'Raíz', kind: 'txt', title: 'llms.txt', path: 'llms.txt', note: 'Entrada reducida para LLMs.' },
    { group: 'Raíz', kind: 'txt', title: 'llms-full.txt', path: 'llms-full.txt', note: 'Contexto ampliado para LLMs.' },
    { group: 'Raíz', kind: 'md', title: 'MCP.md', path: 'MCP.md', note: 'Documento completo de uso MCP.' }
  ];

  const listEl = document.querySelector('#catalogList');
  const searchEl = document.querySelector('#catalogSearch');
  const jumpEl = document.querySelector('#pathInput');
  const groupBtns = Array.from(document.querySelectorAll('[data-group-filter]'));
  const countEl = document.querySelector('#catalogCount');
  const activePathEl = document.querySelector('#activePath');
  const activeTitleEl = document.querySelector('#activeTitle');
  const activeMetaEl = document.querySelector('#activeMeta');
  const viewerBody = document.querySelector('#viewerBody');
  const rawLink = document.querySelector('#openRaw');
  const githubLink = document.querySelector('#openGitHub');
  const copyPathBtn = document.querySelector('#copyPath');
  const statusEl = document.querySelector('#viewerStatus');

  if (!listEl || !searchEl || !jumpEl || !viewerBody || !activePathEl || !activeTitleEl || !activeMetaEl || !rawLink || !githubLink || !copyPathBtn || !statusEl) {
    return;
  }

  let activeGroup = 'all';
  let activePath = '';
  const repoRawBase = 'https://cdn.jsdelivr.net/gh/ateeducacion/normativa_educativa_canaria@main';
  const repoGitHubBase = 'https://github.com/ateeducacion/normativa_educativa_canaria/blob/main';

  const escapeHtml = (value) => value
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;')
    .replaceAll("'", '&#39;');

  const toUrlPath = (repoPath) => repoPath
    .split('/')
    .map((segment) => encodeURIComponent(segment))
    .join('/');

  const resolveRawUrl = (repoPath) => `${repoRawBase}/${toUrlPath(repoPath)}`;
  const resolveGitHubUrl = (repoPath) => `${repoGitHubBase}/${toUrlPath(repoPath)}`;

  const stripFrontmatter = (text) => {
    if (!text.startsWith('---')) return { frontmatter: '', body: text };
    const match = text.match(/^---\s*\n([\s\S]*?)\n---\s*\n?/);
    if (!match) return { frontmatter: '', body: text };
    return {
      frontmatter: match[1].trim(),
      body: text.slice(match[0].length)
    };
  };

  const renderList = () => {
    const term = searchEl.value.trim().toLowerCase();
    const filtered = catalog.filter((item) => {
      const matchesGroup = activeGroup === 'all' || item.group === activeGroup;
      const haystack = [item.title, item.path, item.note, item.group, item.kind].join(' ').toLowerCase();
      const matchesSearch = !term || haystack.includes(term);
      return matchesGroup && matchesSearch;
    });

    listEl.innerHTML = filtered.map((item) => {
      const isActive = item.path === activePath ? 'is-active' : '';
      return `
        <button type="button" class="explorer-item ${isActive}" data-open-path="${escapeHtml(item.path)}">
          <div class="d-flex justify-content-between align-items-start gap-2">
            <div>
              <div class="small text-secondary mb-1">${escapeHtml(item.group)}</div>
              <div class="fw-semibold">${escapeHtml(item.title)}</div>
            </div>
            <span class="badge text-bg-light border text-uppercase">${escapeHtml(item.kind)}</span>
          </div>
          <div class="item-path small text-secondary mt-2">${escapeHtml(item.path)}</div>
          <div class="small mt-2">${escapeHtml(item.note)}</div>
        </button>`;
    }).join('');

    countEl.textContent = `${filtered.length} archivo${filtered.length === 1 ? '' : 's'}`;

    listEl.querySelectorAll('[data-open-path]').forEach((btn) => {
      btn.addEventListener('click', () => openPath(btn.getAttribute('data-open-path') || ''));
    });
  };

  const setActiveButton = () => {
    groupBtns.forEach((btn) => {
      const isActive = btn.dataset.groupFilter === activeGroup;
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', String(isActive));
    });
  };

  const showError = (message) => {
    viewerBody.innerHTML = `<div class="viewer-empty">${escapeHtml(message)}</div>`;
    statusEl.textContent = message;
  };

  const openPath = async (path) => {
    const cleanPath = path.trim();
    if (!cleanPath) return;

    const item = catalog.find((entry) => entry.path === cleanPath);
    activePath = cleanPath;
    renderList();

    activePathEl.textContent = cleanPath;
    activeTitleEl.textContent = item ? item.title : cleanPath.split('/').pop();
    activeMetaEl.textContent = item ? `${item.group} · ${item.kind}` : 'Ruta manual';
    const rawUrl = resolveRawUrl(cleanPath);
    rawLink.href = rawUrl;
    githubLink.href = resolveGitHubUrl(cleanPath);
    jumpEl.value = cleanPath;
    statusEl.textContent = `Abriendo ${cleanPath}`;

    try {
      const response = await fetch(rawUrl, { cache: 'no-store' });
      if (!response.ok) {
        throw new Error(`No se pudo abrir ${cleanPath} (${response.status})`);
      }

      const text = await response.text();
      const ext = cleanPath.split('.').pop().toLowerCase();
      const lineCount = text.split('\n').length;
      activeMetaEl.textContent = `${item ? `${item.group} · ` : ''}${ext.toUpperCase()} · ${lineCount} líneas`;

      if (ext === 'html') {
        viewerBody.innerHTML = '';
        const frame = document.createElement('iframe');
        frame.title = cleanPath;
        frame.src = rawUrl;
        viewerBody.appendChild(frame);
      } else if (ext === 'md' && window.marked) {
        const parts = stripFrontmatter(text);
        const blocks = [];
        if (parts.frontmatter) {
          blocks.push(`
            <details class="mb-3">
              <summary>Frontmatter</summary>
              <pre class="mt-2"><code>${escapeHtml(parts.frontmatter)}</code></pre>
            </details>`);
        }
        blocks.push(`<div class="markdown-view">${window.marked.parse(parts.body)}</div>`);
        viewerBody.innerHTML = blocks.join('');
      } else {
        viewerBody.innerHTML = `<pre><code>${escapeHtml(text)}</code></pre>`;
      }
    } catch (error) {
      showError(error instanceof Error ? error.message : 'No se pudo abrir la ruta solicitada.');
    }
  };

  searchEl.addEventListener('input', renderList);

  groupBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      activeGroup = btn.dataset.groupFilter || 'all';
      setActiveButton();
      renderList();
    });
  });

  jumpEl.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
      event.preventDefault();
      openPath(jumpEl.value);
    }
  });

  document.querySelector('#openPathBtn')?.addEventListener('click', () => openPath(jumpEl.value));
  copyPathBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(activePath || jumpEl.value);
      const previous = copyPathBtn.textContent;
      copyPathBtn.textContent = 'Copiado';
      setTimeout(() => { copyPathBtn.textContent = previous; }, 1200);
    } catch (error) {
      showError('No se pudo copiar la ruta.');
    }
  });

  setActiveButton();
  renderList();
  openPath('06_indices/normativa.yaml');
});
