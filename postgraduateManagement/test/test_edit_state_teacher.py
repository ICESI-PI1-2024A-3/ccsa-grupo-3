from django.test import TestCase
from django.urls import reverse
from postgraduateManagement.models import Docente, Ciudad
from django.http import HttpResponseRedirect

class DocenteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Configurar datos de prueba una vez para toda la TestCase
        ciudad = Ciudad.objects.create(id=1, nombre='Ciudad de Ejemplo')
        cls.docente = Docente.objects.create(
            cedula='1234567890', 
            nombre='Juan', 
            apellido='Pérez', 
            email='juan@example.com',
            telefono=123456789, 
            ciudad=ciudad
        )

    def test_get_object(self):
        # Verificar si la función get_object devuelve el Docente correcto
        response = self.client.get(reverse('state', kwargs={'cedula': self.docente.cedula}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['docente'], self.docente)

    def test_template_used(self):
        # Verificar si se está utilizando el template correcto
        response = self.client.get(reverse('state', kwargs={'cedula': self.docente.cedula}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'postgraduateManagement/../edit_state_teacher.html')

 
def test_status_update_successfully(self):
        # Simular la actualización del estado del docente
        new_estado = 'Inactivo'
        response = self.client.post(reverse('state', kwargs={'cedula': self.docente.cedula}), {'estado': new_estado})
    
         # Verificar que la vista redirige correctamente después de la actualización
        self.assertEqual(response.status_code, 302)  # Verificar código de redirección
        self.assertEqual(response.url, reverse('teachers'))  # Verificar URL de redirección

        # Verificar que el estado se haya actualizado correctamente en la base de datos 
        updated_docente = Docente.objects.get(cedula=self.docente.cedula)
        self.assertEqual(updated_docente.estado, new_estado)
