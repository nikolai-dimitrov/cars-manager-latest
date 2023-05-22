const carModelsPath = '/vehicle/api';
// const host = 'http://127.0.0.1:8000';
// const host = 'http://localhost:81';
const host = 'https://cars-manager.tk';
const options = [];


async function setModel() {
    unsetModels();
    const carField = document.querySelector('.car');
    const modelField = document.querySelector('.model');
    const car = carField[carField.value].innerText;
    let carModels = await getCarModels(car);
    carModels = carModels.map(el => el.model);

    for (let o of options) {
        if (carModels.includes(o.innerText) || o.innerText === '---------')
            modelField.appendChild(o);
    }
}


function unsetModels() {
    const modelField = document.querySelector('.model');
    const opt = Array.from(modelField.getElementsByTagName('option'));

    for (let o of opt) {
        if (!(options.includes(o))) {
            options.push(o);
        }
        modelField.removeChild(o);
    }

    return options;
}


async function getCarModels(car) {
    return await get(`${carModelsPath}/?car=${car}`);
}


function getInit(method, data) {
    const init = {
        'method': method,
        'headers': {}
    }

    if (data) {
        init.headers['Content-Type'] = 'application/json';
        init.body = JSON.stringify(data)
    }

    return init;
}


async function request(path, init) {
    const url = `${host}${path}`;

    try {
        const response = await fetch(url, init);

        if (!response.ok) {
            const data = await response.json();
            throw new Error(data.message);
        }

        if (response.status === 204) {
            return response
        } else {
            return response.json();
        }

    } catch (error) {
        alert(error.message);
        console.log(error.message);
        throw error;
    }
}


async function get(path) {
    return await request(path, getInit('GET'));
}

function setRequired() {
    const fields = document.querySelectorAll('.ad-form-field');
    Array.from(fields).forEach(el => el.required = false);
    getSearchedModelFromSession()
}

// Images slide show
function addClasses() {
    let otherImages = Array.from(document.querySelectorAll('.img-container li'));
    let allImg = Array.from(document.querySelectorAll('.img-container li img'));
    for (let i = 0; i < allImg.length; i++) {
        allImg[i].id = `${i + 1}`;
    }
    otherImages.splice(0, 1);
    for (let i = 0; i < otherImages.length; i++) {
        otherImages[i].classList.add(`image${i}`);
    }
}

let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    addClasses();
    let i;
    let slides = document.getElementsByClassName("mySlides");
    // let slides = document.querySelectorAll('.mySlides');
    let dots = document.getElementsByClassName("dot");
    if (n > slides.length) {
        slideIndex = 1
    }
    if (n < 1) {
        slideIndex = slides.length
    }
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex - 1].style.display = "block";
    dots[slideIndex - 1].className += " active";
    attachEventOnImage();
}

function changeClickedImg(event) {
    let idAsNumber = Number(event.target.id)
    currentSlide(idAsNumber)
}

function attachEventOnImage() {
    let otherImages = Array.from(document.querySelectorAll('.img-container li'));
    for (let i = 0; i < otherImages.length; i++) {
        otherImages[i].addEventListener('click', changeClickedImg)
    }
}

// Other
function getSearchedModelFromSession() {
    let formSearchBtn = document.getElementsByClassName('search-form-btn')[0];
    if (sessionStorage.getItem('currentCar')) {
        let searchedCarName = sessionStorage.getItem('currentCar').toLowerCase();
        let carSelectField = document.getElementById('id_car')
        let carOptions = Array.from(carSelectField.querySelectorAll('option'));
        carOptions.forEach(function (x) {
            if (x.textContent.toLowerCase() === searchedCarName) {
                x.selected = true
            }
            formSearchBtn.click();
            sessionStorage.removeItem('currentCar');
        })
    }
}

// Images
function imageHasChanged(event) {
    let selectedFile = event.target.files[0];
    let img = event.target.parentElement.parentElement.querySelector('img');
    let reader = new FileReader();
    reader.onload = function () {
        img.src = this.result
    }
    reader.readAsDataURL(selectedFile);
}

function imageOnClick(event) {
    let container = event.target.parentElement
    let inputField = container.querySelector('div input[type=file]');
    inputField.click();
}

function profileImageHasChanged(event) {
    let selectedFile = event.target.files[0];
    let img = document.getElementById('profile-image')
    let reader = new FileReader();
    reader.onload = function () {
        img.src = this.result
    }
    reader.readAsDataURL(selectedFile);
}

function imageOnClickProfile(event) {
    const inputField = document.getElementById('image');
    inputField.click();
}

