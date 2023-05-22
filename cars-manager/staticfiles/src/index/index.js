window.onload = changeData
function changeData() {
    if (document.getElementsByClassName('card__search-btn')[0] !== undefined) {
        Array.from(document.getElementsByClassName('card__search-btn')).forEach(x => x.addEventListener('click', searchBtnHandler))

    }
    let transmissionSelect = document.getElementById('id_transmission');
    let fuelSelect = document.getElementById('id_fuel_type');
    let cylindersSelect = document.getElementById('id_cylinders');
    transmissionSelect.querySelectorAll('option')[0].textContent = 'Transmission/All'
    fuelSelect.querySelectorAll('option')[0].textContent = 'Fuel/All'
    cylindersSelect.querySelectorAll('option')[0].textContent = 'Cylinders/All'

    let transmissionFieldsList = document.getElementsByClassName('transmission');
    for (const field of transmissionFieldsList) {
        if (field.textContent.trim() === 'a') {
            field.textContent = 'Automatic';
        } else if (field.textContent.trim() === 'm') {
            field.textContent = 'Manual';
        }
    }
}

function searchBtnHandler(event) {
    let carMakeName = event.target.parentElement.parentElement.querySelector('body h3').textContent.split(' ')[0];
    window.sessionStorage.setItem('currentCar', `${carMakeName}`);
}


function clearIndexCachedInfo(event) {
    const inputCheckBoxEl = document.getElementById('CacheInput');
    const carBrandInput = document.getElementById('id_make');
    const buttonSearch = document.getElementsByClassName('search-button-home')[0];
    const resultEl = document.getElementsByClassName('results')[0]
    const paginatotionEl = document.getElementsByClassName('pagination-background')[0]
    inputCheckBoxEl.checked = sessionStorage.getItem('cacheIndexPage') !== 'false';
    if ((sessionStorage.getItem('cacheIndexPage') === 'false') && (sessionStorage.getItem('navIndexClicked') === 'true')) {
        resultEl.remove();
        paginatotionEl.remove()
        carBrandInput.value = 'None';
        sessionStorage.setItem('navIndexClicked', 'false');
        buttonSearch.click();
    }

}


function checkBoxHandler(event) {
    if (event.target.checked === true) {
        sessionStorage.setItem('cacheIndexPage', 'true');
    } else if (event.target.checked === false) {
        sessionStorage.setItem('cacheIndexPage', 'false');
    }
}

clearIndexCachedInfo();




