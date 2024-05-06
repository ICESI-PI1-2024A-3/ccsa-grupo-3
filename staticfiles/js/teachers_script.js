const triggers = document.querySelectorAll('.trigger');
    triggers.forEach(trigger => {
        trigger.addEventListener('click', function(event) {
            event.preventDefault();
            const card = this.closest('.card');
            card.classList.toggle('show');
        });
});

/*
const trigger = document.querySelector('.trigger'),
addclass = document.querySelector('.card');
trigger.addEventListener('click', function(event) {
    event.preventDefault();
    addclass.classList.toggle('show');
});
*/

function copy_teacher_email(cedula) {
    var copyText = document.getElementById(cedula);
    copyText.select();
    copyText.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(copyText.value);
    alert("Copied the text: " + copyText.value);
}
