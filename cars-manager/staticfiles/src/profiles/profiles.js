function changeCreateProfileNav() {
    let anchor = document.getElementsByClassName('item')[0].querySelector('a');
    anchor.id = 'createProfileA';

    anchor.classList.add('choosen_item_nav')
    anchor.classList.remove('mini-nav__items')
    let miniNav = document.getElementsByClassName('mini-nav')[0];
    miniNav.style.width = '19%';
}
changeCreateProfileNav();