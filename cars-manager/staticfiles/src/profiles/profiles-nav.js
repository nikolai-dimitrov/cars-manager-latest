// import {clearIndexCachedInfo} from "../index";

function highlightField() {
    let ulContainerNav = document.getElementsByClassName('mini-nav__items')[0];
    ulContainerNav.addEventListener('click', addAnchorTextContent);
    let allAnchors = Array.from(document.querySelectorAll('.mini-nav__items a'));
    for (let anchor of allAnchors) {
        if (anchor.textContent === sessionStorage.getItem('clickedAnchor')) {
            anchor.classList.add('choosen_item_nav');
        }
        if (anchor.textContent === 'Create Profile') {
            changeNavStyles(anchor)
        }
    }
}

function highlightEditAnchor() {
    sessionStorage.setItem('clickedAnchor', 'Edit Profile')
}

function addAnchorTextContent(event) {
    if (event.target.textContent === 'Send Delete Code') {
        sessionStorage.setItem('clickedAnchor', 'Delete Profile');
    } else {
        sessionStorage.setItem('clickedAnchor', event.target.textContent);
    }
}

function changeNavStyles(el) {
    let width = innerWidth;
    if (width <= 461) {
        let divElementNavWrapper = document.getElementsByClassName('mini-nav')[0];
        divElementNavWrapper.style.width = '50%';
    }
}

// Main NAV //
function clearIndexPage(event) {
    document.getElementsByClassName('results')[0].remove();
    document.getElementsByClassName('pagination-background')[0].remove();
}

function addIndexCacheInSession(event) {
    if (sessionStorage.getItem('cacheIndexPage') === null) {
        sessionStorage.setItem('cacheIndexPage', 'false');
    }
}

function onClickIndexPage(event) {
    sessionStorage.setItem('navIndexClicked', 'true');
    sessionStorage.setItem('searching', `false`);
}ii

addIndexCacheInSession();