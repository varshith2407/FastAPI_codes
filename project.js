async function fetchDeals() {
  const response = await fetch('/deals');
  const deals = await response.json();

  const dealList = document.getElementById('deal-list');
  deals.forEach(deal => {
    const listItem = document.createElement('li');
    listItem.textContent = `${deal.id}: ${deal.title} (${deal.stage})`;
    dealList.appendChild(listItem);
  });
}

fetchDeals();
