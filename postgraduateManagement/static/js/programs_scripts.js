function showInfo(codigo) {
    // Obtiene la información del programa seleccionado
    var info = document.getElementById('info' + codigo).innerHTML;
    // Obtiene el elemento wrapperInfo
    var wrapperInfo = document.getElementById('wrapperInfo');
    // Obtiene los elementos hijos de wrapperInfo
    var children = wrapperInfo.children;
    // Agrega la clase 'hidden' a los elementos hijos para ocultar el contenido
    for (var i = 0; i < children.length; i++) {
        children[i].classList.remove('visible');
    }
    // Espera 0.5 segundos para que se realice la transición
    setTimeout(function() {
        // Cambia el contenido
        wrapperInfo.innerHTML = info;
        // Quita la clase 'hidden' a los elementos hijos para mostrar el nuevo contenido
        var newChildren = wrapperInfo.children;
        for (var i = 0; i < newChildren.length; i++) {
            newChildren[i].classList.add('visible');
        }
    }, 100);
}