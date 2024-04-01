# Plan de Pruebas para Vistas

## Pruebas unitarias para las vistas:

### setUp
- [x] Crear una ciudad de prueba.
- [x] Crear una facultad de prueba.
- [x] Crear un tipo de programa de prueba.
- [x] Crear un director de prueba.
- [x] Crear un programa de prueba.
- [x] Crear un usuario para las pruebas.

### subject_list_view
- [x] Prueba que la vista de lista de materias carga correctamente y utiliza el template adecuado.

### course_view
- [x] Prueba que la vista de lista de cursos carga correctamente y utiliza el template adecuado.

### course_view_with_material_code
- [x] Prueba que la vista de lista de cursos carga correctamente para un código de materia dado.
- [x] Asegura que solo los cursos con el código de materia correcto se muestren en la lista.

### course_view_with_nonexistent_material_code
- [x] Prueba que la vista de lista de cursos carga correctamente para un código de materia inexistente.
- [x] Asegura que no se encuentren cursos en la lista.

### course_delete_view
- [x] Prueba la eliminación de un curso existente.

### nonexistent_course_delete_view
- [x] Prueba que se devuelve un error 404 para el intento de eliminación de un curso inexistente.

### course_update_view
- [x] Prueba la actualización de un curso existente.

### invalid_course_update_view
- [x] Prueba la actualización de un curso con datos inválidos.

### duplicate_group_course_update_view
- [x] Prueba que la actualización de un curso con un grupo duplicado redirige de nuevo al formulario de edición.

### course_create_view
- [x] Prueba la creación de un nuevo curso.

### invalid_course_create_view
- [x] Prueba la creación de un curso con datos inválidos.

### duplicate_course_create_view
- [x] Prueba que la creación de un curso con una clave primaria duplicada redirige a la misma página de creación.

### programs_view_get
- [x] Prueba que la vista de programas de posgrado se carga correctamente mediante una solicitud GET.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que se carguen los programas de posgrado correctamente.

### programs_view_post
- [x] Prueba que la vista de programas de posgrado responde correctamente a una solicitud POST.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que el programa seleccionado coincida con el programa esperado.

### teacher_view
- [x] Prueba que la vista de docentes se carga correctamente mediante una solicitud GET.
- [x] Asegura que se utilice el template adecuado.

### teacher_filter_by_city1
- [x] Prueba que la vista de docentes filtra correctamente los docentes por ciudad 1 y estado activo.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que todos los docentes en la lista sean de la ciudad 1 y estén en estado activo.

### teacher_filter_by_city2
- [x] Prueba que la vista de docentes filtra correctamente los docentes por ciudad 2 y estado activo.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que todos los docentes en la lista sean de la ciudad 2 y estén en estado activo.

### teacher_filter_by_status
- [x] Prueba que la vista de docentes filtra correctamente los docentes por estado inactivo.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que todos los docentes en la lista estén en estado inactivo.

### teacher_filter_by_search1
- [x] Prueba que la vista de docentes filtra correctamente los docentes por el nombre "Test1" y estado activo.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que todos los docentes en la lista contengan "Test1" en su nombre y estén en estado activo.

### teacher_filter_by_search2
- [x] Prueba que la vista de docentes filtra correctamente los docentes por el nombre "Test3" y estado activo.
- [x] Asegura que se utilice el template adecuado.
- [x] Verifica que todos los docentes en la lista contengan "Test3" en su nombre y estén en estado activo.

### vista_programa_posgraduados
- [x] Prueba que la vista de un programa de posgrado se carga correctamente.
- [x] Asegura que se devuelva el código de estado 200.

### codigo_programa_inexistente
- [x] Prueba que se redirige correctamente cuando se intenta acceder a un programa de posgrado inexistente.
- [x] Asegura que se devuelva el código de estado 302.

### test3
- [x] Prueba que la vista de edición de un director se carga correctamente.
- [x] Asegura que se devuelva el código de estado 200.

### test_editing_director_post
- [x] Prueba que la vista de edición de un director responde correctamente a una solicitud POST.
- [x] Asegura que se devuelva el código de estado 302.
- [x] Verifica que los datos del director se hayan actualizado correctamente en la base de datos.

#### test_login_required
- [x] Verificar que se pueda iniciar sesión con un usuario existente.

#### test_login_with_nonexistent_user
- [x] Verificar que no se pueda iniciar sesión con un usuario inexistente y que se redireccione al formulario de inicio de sesión.