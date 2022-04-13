let fromLeft = "fromLeft 1s ease 0s 1 normal forwards";
let fromRight = "fromRight 1s ease 0s 1 normal forwards";
let num = 1;
let nextButton = document.getElementsByClassName('next-button')[0];
let prevButton = document.getElementsByClassName('prev-button')[0];

prevButton.setAttribute("disabled", "disabled");

document.getElementsByClassName('test-wrap-1')[0].style.animation = fromRight;

nextButton.onclick = function () {
    if (num == 4) {
        nextButton.innerHTML = 'Готово';
    }
    if (num == 5) {
        alert('Thanks')
        document.getElementsByClassName('test-wrap-' + num)[0].style.display = "none";
        num++;
        return 0;
    }
    document.getElementsByClassName('test-wrap-' + num)[0].style.display = "none";
    num++;
    document.getElementsByClassName('test-wrap-' + num)[0].style.animation = fromRight;
    document.getElementsByClassName('test-wrap-' + num)[0].style.display = "flex";
};

prevButton.onclick = function () {
    if (num == 5) {
        nextButton.innerHTML = 'Дальше';
    }
    if (num == 1) {
        return 0;
    }
    if (num != 6) {
        document.getElementsByClassName('test-wrap-' + num)[0].style.display = "none";
    }

    num--;
    document.getElementsByClassName('test-wrap-' + num)[0].style.animation = fromLeft;
    document.getElementsByClassName('test-wrap-' + num)[0].style.display = "flex";
};