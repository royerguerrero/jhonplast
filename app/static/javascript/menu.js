const header = document.querySelector(".header")
const menuItems = header.querySelectorAll('.navbar__item')

menuItems.forEach(item => {
    if (item.href == window.location) {
        item.classList.add('navbar__item--active')
    }
})

const burgerButton = document.querySelector('.navbar__toogle-button')
let isMenuOpen = false

burgerButton.addEventListener('click', () => {
    burgerButton.classList.toggle("navbar__toogle-button--close")

    if (isMenuOpen) {
        isMenuOpen = false
    } else {
        isMenuOpen = true
        menuItems.forEach(i => {i.classList.add('hide')})
    }

   menuItems.forEach(item => item.classList.toggle("show"))
})