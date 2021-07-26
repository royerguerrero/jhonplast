const url = new URL(window.location)
const category = url.searchParams.get('category')

if (category) {
    const pills = document.querySelectorAll('.pill')
    pills.forEach(pill => {
        if (pill.textContent.toLowerCase() === category.toLowerCase()) {
            pill.classList.add('pill--active')
        }
    })
}

const search = url.searchParams.get('s')

if (search) {
    const searchInput = document.querySelector('input[name=s]')
    searchInput.value = search

    const productsCollection = document.querySelector('.products__collection')
    const productCards = productsCollection.querySelectorAll('.card--product')

    if (productCards.length < 1) {
        productsCollection.innerHTML = '<p class="products__empty">No se encontro ningun producto.</p>'
    }    
}
