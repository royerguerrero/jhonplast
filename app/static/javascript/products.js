// const categoryGetParam 
const url = new URL(window.location)
const category = url.searchParams.get('category')

const pills = document.querySelectorAll('.pill')
pills.forEach(pill => {
    if (pill.textContent.toLowerCase() === category.toLowerCase()) {
        pill.classList.add('pill--active')
    }
})

const searchProducts = query => {
    
}