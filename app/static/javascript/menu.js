const menuItems = document.querySelectorAll('.navbar__item')


menuItems.forEach(item => {
    if (item.href == window.location) {
        item.classList.add('navbar__item--active')
    }
})