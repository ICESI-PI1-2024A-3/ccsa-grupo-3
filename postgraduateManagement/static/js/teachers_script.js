const trigger = document.querySelector('.trigger'),
addclass = document.querySelector('.card');
trigger.addEventListener('click', function() {
    addclass.classList.toggle('show');
})