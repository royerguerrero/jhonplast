const tabs = document.querySelector('.tabs')
const tabsItems = tabs.querySelectorAll('.tabs__item')
const tabsParagraphs = tabs.querySelectorAll('.tabs__paragraph')

tabsParagraphs[0].classList.add('show')

tabsItems.forEach(tabItem => {
    tabItem.addEventListener('click', () => {
        const currentTab = tabs.querySelector('.tabs__item--active')
        currentTab.classList.remove('tabs__item--active')
        tabItem.classList.add('tabs__item--active')

        tabsParagraphs.forEach(paragraph => {
            paragraph.classList.remove('show')
        })

        const selectedTabContent = tabsParagraphs[tabItem.dataset.id]
        selectedTabContent.classList.add('show')
    }) 
}) 