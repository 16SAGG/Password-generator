let show_btn = document.getElementById("show_btn");
let show_elmnt = document.getElementById("show_elmnt");

show_btn.addEventListener('click', toggleDiv);

function toggleDiv() {
    show_btn.classList.toggle('hide');
    show_elmnt.classList.toggle('hide');
}