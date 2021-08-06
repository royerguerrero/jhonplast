const menuItems = document.querySelectorAll('.navbar__item')

menuItems.forEach(item => {
    if (item.href == window.location) {
        item.classList.add('navbar__item--active')
    }
})

const burgerButton = document.querySelector('.navbar__toogle-button')
burgerButton.addEventListener('click', () => {
    // TODO: Add logic for show or not the navbar
})