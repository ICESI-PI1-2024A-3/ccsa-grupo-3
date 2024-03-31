# Contribuir al Proyecto

Como contribuidor del proyecto debes tomar en cuenta las siguientes reglas.

- [Code Style](#code-style)
- [Estructura del proyecto](#project)
  - [Notación de los archivos](#files)
  - [Notación de las clases](#class)
  - [Notación de los métodos](#methods)
- [Estructura de los commits](#commits)

Recuerde que todo lo que no sea visible para el usuario debe ser escrito en **INGLES** (cosas como: nombre de variables/clases/archivos, sintaxis de los commits, etc.) y todo lo que si pueda observar el cliente se debe redactar en **ESPAÑOL** (por colocar algunos ejemplos: alertas, models, documentación, etc.)

## <a name="code-style"></a> Code Style

Para el código estaremos usando el code style <a href="https://peps.python.org/pep-0008/">PEP-8</a>, cabe recalcar que aunque la mayoría de editores de código tengan extensiones que verifiquen este code style, dichas extensiones no son infalibles, por lo tanto se recomienda que revisen detenidamente la documentación.

## <a name="project"></a> Estructura del proyecto

Para la estructuración del proyecto se usara la notación **Húngara**`, la cual consiste en que la primera palabra tenga inicio en minúscula mientras que las demás palabras tengan la primera letra en mayúscula:

```
manageApplicationStandard/
exampleProjectForDemonstration/
startProject/
```

Ademas, se recomienda que cada aplicación tenga las carpetas que sean pertinentes para mantener un orden.

```
  ├── projectName/
  │       ├─ static/
  │       │    ├─ css/
  │       │    └─ js/
  │       │
  │       └─ models/
  ...
```

#### <a name="files"></a> Notación de los archivos

Para los archivos estaremos usando la notación **snake_case**, la cual consiste que que todas las palabras estén en minúscula y separadas por un guion (-).

```
file_example.txt
week_01.md
hello_world.html
```

Ademas, se recomienda que si los archivos tienen una lata correlación entre si (por ejemplo: html, css y js) estos deben tener el mismo nombre del archivo "principal" seguido por una redundancia.

```
├── projectName/
│       ├─ static/
│       │    ├─ css/
│       │    │   └─ hello_world_styles.css
│       │    └─ js/
│       │        └─ hello_world_functions.js
│       │
│       └─ models/
│            └─ hello_world.html ⪡────────── archivo "principal"
...
```

#### <a name="class"></a> Notación de las clases

Para las clases se usara la notación **CamelCase**, la cual consiste en que cada palabra inicie con la su letra en mayúscula.

```py
class TestPersona:
    ...

class LongNameClassForExample:
    ...

class Example:
    ...
```

#### <a name="methods"></a> Notación de los métodos

Para las clases se usara la notación **snake_case**, la cual consiste que que todas las palabras estén en minúscula y separadas por un guion (-).

```py
def start_test(int count):
    ...

def long_definition_for_example(str log_name):
    ...

def example(int short_name):
    ...
```

## <a name="commits"></a> Estructura de los Commits

### Sintaxis Commits

Para los commits debemos tenemos un formato predefinido, esto con el propósito de generar commits mas amigables para la lectura.
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
  │       │              empezando en minúscula y no tener un punto al final
  │       │
  │       └─⫸ Si este commit permite marcar como completa una HU/Instancia
  │            entonces debe colocar el identificador de la HU/Instancia completada.
  │
  └─⫸ Tipo de Commit: build|docs|feat|fix|perf|refactor|test
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
- **test**: agregar pruebas faltantes o corregir las pruebas existentes

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
