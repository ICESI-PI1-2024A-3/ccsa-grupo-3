# Contribuir al Proyecto

Como contribuidor del proyecto debes tomar en cuenta las siguientes reglas.

 - [Code Style](#code-style)
 - [Estructura del proyecto](#project)
 - [Estructura de los archivos](#files)
 - [Estructura de los commits](#commits)
 
Recuerde que todo lo que no sea visible para el usuario debe ser escrito en **INGLES** (cosas como: nombre de variables/clases/archivos, sintaxis de los commits, etc.) y todo lo que si pueda observar el cliente se debe redactar en **ESPAÑOL** (prints por consola, models, documentación, etc.)

##<a name="code-style"></a> Code Style

##<a name="project"></a> Estructura del proyecto

##<a name="files"></a> Estructura de los archivos

##<a name="commits"></a> Estructura de los Commits

Para los commits debemos tenemos un formato predefinido, esto con el propósito de generar commits mas amigables para la lectura.

### Sintaxis Commits

Cada commit consiste en un **encabezado** y una **descripción**.

```
<encabezado>
<ESPACIO EN BLANCO>
<descripción>
```

Los encabezados tienen un formato especial que consiste en **tipos**, **hu** y una **descripción**.

El `encabezado` es de carácter obligatorio y siguiendo el [Formato Encabezado](#formato-encabezado).

La `descripción` es de carácter obligatorio para todos los commits excepto aquellos que sean de tipo "docs". Cuando la descripción esta en uso, esta debe de tener por lo menos 20 caracteres de largo y seguir el [Formato Descripción](#formato-desc)

#### <a name="formato-encabezado"></a> Formato Encabezado

```
<tipo>(<hu>): <resumen>
  │       │         │
  │       │         └─⫸ El resumen debe ser un imperativo,
  │       │              empezando en minúscula y no tener un punto al final.
  │       │
  │       └─⫸ Si este commit permite marcar como completa una HU/Instancia
  │            entonces debe colocar el identificador HU/Instancia completada.
  │
  └─⫸ Tipo de Commit: build|ci|docs|feat|fix|perf|refactor|test
```

Los campos `<tipo>` y `<resumen>` son de carácter obligatorio, el campo `<hu>` solamente es obligatorio en caso de que el commit permita marcar una historia de usuario/instancia como **completada**.

##### Tipo

Este campo puede tener una de las siguientes opciones:

- **build**: cambios que afectan el sistema de compilación o dependencias externas (ejemplos: models, una nueva app, establecer una carpeta views en vez de solamente views.py)
- **docs**: cambios realizados unicamente en la documentación
- **feat**: una nueva funcionalidad/característica (ejemplo: visualizar profesores, crear una nueva programación, editar la información de un profesor)
- **fix**: una corrección de un error
- **perf**: un cambio en el código que mejora el rendimiento
- **refactor**: un cambio en el código que no corrige un error ni agrega una funcionalidad (cambiar el nombre de una variable/clase/archivo)
- **test**: agregar las pruebas faltantes o corregir las pruebas existentes

##### Hu

Esta campo es obligatorio solamente si el commit permite marcar una historia de usuario/instancia como **completada**, en caso de que se cumpla esta condición el campo puede tener una de las siguientes opciones:

- **HU-00**: si lo que se completo fue una historia de usuario se debe colocar el identificador de la misma, este identificador debe ser de 2 dígitos (ejemplo: 01, 12, 05, 09)
- **HU-00 | 00**: si lo se completo fue una instancia, estaba debe tener el identificador de la historia de usuario y su propio identificador, estos identificadores también deben ser de 2 dígitos.

##### Resumen

En este cambo se debe incluir un resumen del cambio realizado donde:

- se debe usar un imperativo, en tiempo presente "cambia" no "cambió" ni "cambiar"
- **no** escriba la primera la primera letra en mayúscula
- sin punto (.) al final

#### <a name="formato-desc"></a> Formato Descripción

Al igual que en el resumen, se debe usar un imperativo, en tiempo presente "arregla" no "arreglar" ni "arreglado".

En este campo debe explicar la motivación del cambio. Este mensaje de confirmación debe explicar por qué se realiza el cambio. Puedes incluir una comparación del comportamiento anterior con el nuevo para ilustrar el impacto del cambio.
