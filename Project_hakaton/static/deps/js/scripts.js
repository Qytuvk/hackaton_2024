const navbarMenu = document.querySelector(".navbar .links");
const hamburgerBtn = document.querySelector(".hamburger-btn");
const hideMenuBtn = navbarMenu.querySelector(".close-btn");
const showPopupBtn = document.querySelector(".login-btn");
const formPopup = document.querySelector(".form-popup");
const hidePopupBtn = formPopup.querySelector(".close-btn");
const signupLoginLink = formPopup.querySelectorAll(".bottom-link a");
const emailInput = document.getElementById('EmailTextField').querySelector('input[type="text"]');




document.getElementById('EntryButton').onclick = IsValid;

function IsValid() {
    const email = emailInput.value;

    if (isValidEmail(email)){
        //образщение к бд
       window.location.href = "http://127.0.0.1:8000/";

    }    
    else{
        alert("Неверный email")
    }

}




// Show mobile menu
hamburgerBtn.addEventListener("click", () => {
    navbarMenu.classList.toggle("show-menu");
});


// Hide mobile menu
hideMenuBtn.addEventListener("click", () =>  hamburgerBtn.click());

// Show login popup
showPopupBtn.addEventListener("click", () => {
    document.body.classList.toggle("show-popup");
});

// Hide login popup
hidePopupBtn.addEventListener("click", () => showPopupBtn.click());

// Show or hide signup form
signupLoginLink.forEach(link => {
    link.addEventListener("click", (e) => {
        e.preventDefault();
        formPopup.classList[link.id === 'signup-link' ? 'add' : 'remove']("show-signup");
    });
});



function isValidEmail(email) {
    flag = false;
    arr = [".com", ".org", ".net", ".int", ".edu", ".gov", ".mil"];

    for (let i = 0; i < 7; i++) {
        if (email.includes(arr[i])){
            flag = true;
            break;
        }
      }

    const re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase()) && flag;

  }

function CheckEmail(email){
    console.log(1);

    if (isValidEmail(email)){
    }
    else{

    }
}

document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var fileInput = document.getElementById('file-input');
    var file = fileInput.files[0];

    if (file) { // Проверяем, выбран ли файл
        var formData = new FormData();
        formData.append('file', file);

        fetch('/upload/', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        });
    } else {
        console.log('Файл не выбран');
    }
});