document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#cardFilter');
  const items = Array.from(document.querySelectorAll('.filter-item'));
  const emptyState = document.querySelector('#noResults');

  if (!input || !items.length || !emptyState) {
    return;
  }

  const applyFilter = () => {
    const term = input.value.trim().toLowerCase();
    let visible = 0;

    items.forEach((item) => {
      const haystack = (item.dataset.search || '').toLowerCase();
      const match = !term || haystack.includes(term);
      item.classList.toggle('is-hidden', !match);
      if (match) visible += 1;
    });

    emptyState.classList.toggle('d-none', visible !== 0);
  };

  input.addEventListener('input', applyFilter);
  applyFilter();
});
