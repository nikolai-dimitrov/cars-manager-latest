function openPopup(event) {
    let hiddenDiv = event.target.parentElement.parentElement.querySelector('.range')
    hiddenDiv.classList.remove('range')
    hiddenDiv.classList.add('range-activate')
    slidersControls(event)
}

function closePopup(event) {
    console.log(event.target.parentElement.parentElement)
    let hiddenDiv = event.target.parentElement.parentElement
    hiddenDiv.classList.remove('range-activate')
    hiddenDiv.classList.add('range')
}

function slidersControls(event) {
    let slidersDivContainer = event.target.parentElement.nextElementSibling;
    let yearsSlider = false;
    if (event.target.classList[0] === 'years') {
        yearsSlider = true;
    }
    let rangeMin = 1;
    const range = slidersDivContainer.querySelector(".range-selected");
    const rangeInput = slidersDivContainer.querySelectorAll(".range-input input");
    const rangePrice = slidersDivContainer.querySelectorAll(".range-price input");

    rangeInput.forEach((input) => {
        input.addEventListener("input", (e) => {
            let minRange = parseInt(rangeInput[0].value);
            let maxRange = parseInt(rangeInput[1].value);
            if (maxRange - minRange < rangeMin) {
                if (e.target.className === "min") {
                    rangeInput[0].value = maxRange - rangeMin;
                } else {
                    rangeInput[1].value = minRange + rangeMin;
                }
            } else {
                rangePrice[0].value = minRange;
                rangePrice[1].value = maxRange;
                if (yearsSlider === false) {
                    range.style.left = (minRange / rangeInput[0].max) * 100 + "%";
                    range.style.right = 100 - (maxRange / rangeInput[1].max) * 100 + "%";
                } else {
                    let yearPercent = 1;
                    let leftPercents = rangeInput[0].max - rangePrice[0].value;
                    range.style.left = 100 - leftPercents + "%";

                    let rightPercent = rangeInput[1].max - rangePrice[1].value
                    range.style.right = rightPercent + "%"
                }
            }
        });
    });
    rangePrice.forEach((input) => {
        input.addEventListener("input", (e) => {
            let minPrice = rangePrice[0].value;
            let maxPrice = rangePrice[1].value;
            if (maxPrice - minPrice >= rangeMin && maxPrice <= rangeInput[1].max) {
                if (e.target.className === "min") {
                    rangeInput[0].value = minPrice;
                    range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
                } else {
                    rangeInput[1].value = maxPrice;
                    range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
                }
            }
        });
    });
}

// let rangeMin = 100;
// const range = document.querySelector(".range-selected");
// const rangeInput = document.querySelectorAll(".range-input input");
// const rangePrice = document.querySelectorAll(".range-price input");
//
// rangeInput.forEach((input) => {
//     input.addEventListener("input", (e) => {
//         let minRange = parseInt(rangeInput[0].value);
//         let maxRange = parseInt(rangeInput[1].value);
//         if (maxRange - minRange < rangeMin) {
//             if (e.target.className === "min") {
//                 rangeInput[0].value = maxRange - rangeMin;
//             } else {
//                 rangeInput[1].value = minRange + rangeMin;
//             }
//         } else {
//             rangePrice[0].value = minRange;
//             rangePrice[1].value = maxRange;
//             range.style.left = (minRange / rangeInput[0].max) * 100 + "%";
//             range.style.right = 100 - (maxRange / rangeInput[1].max) * 100 + "%";
//         }
//     });
// });
// rangePrice.forEach((input) => {
//     input.addEventListener("input", (e) => {
//         let minPrice = rangePrice[0].value;
//         let maxPrice = rangePrice[1].value;
//         if (maxPrice - minPrice >= rangeMin && maxPrice <= rangeInput[1].max) {
//             if (e.target.className === "min") {
//                 rangeInput[0].value = minPrice;
//                 range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
//             } else {
//                 rangeInput[1].value = maxPrice;
//                 range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
//             }
//         }
//     });
// });
