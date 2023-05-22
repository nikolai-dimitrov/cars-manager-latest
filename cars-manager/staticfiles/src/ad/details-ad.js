function changeImageProperty() {
    let mainElement = document.querySelector('main');

    let allImages = Array.from(mainElement.getElementsByTagName('IMG'));

    allImages.forEach(function (x) {
        let srcList = x.src.split('/');
        let srcName = srcList[srcList.length - 1];
        if (srcName.includes('no-image-icon')) {
            x.style.objectFit = 'contain';
        } else {
            x.style.objectFit = 'cover';
        }
    });
    console.log('work');
}
changeImageProperty();