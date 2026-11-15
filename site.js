'use strict';
const filters = document.querySelector('.filters');
const buttons = [...document.querySelectorAll('[data-filter]')];
const cards = [...document.querySelectorAll('[data-category]')];
const status = document.querySelector('#filter-status');
if (filters && status) {
  filters.hidden = false;
  buttons.forEach(button => button.addEventListener('click', () => {
    const category = button.dataset.filter;
    let count = 0;
    cards.forEach(card => {
      card.hidden = category !== 'All' && card.dataset.category !== category;
      if (!card.hidden) count++;
    });
    buttons.forEach(item => {
      item.classList.toggle('active', item === button);
      item.setAttribute('aria-pressed', String(item === button));
    });
    status.hidden = false;
    status.textContent = `${count} ${count === 1 ? 'project' : 'projects'} shown`;
  }));
}
