from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse


class LoginTestCase(TestCase):
    def setUp(self):
        # Creamos un usuario para las pruebas
        self.username = 'testuser'
        self.password = 'testpassword'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_required(self):
        # Creamos un cliente de prueba
        client = Client()

        # Iniciar sesión con el usuario creado
        logged_in = client.login(username=self.username, password=self.password)
        self.assertTrue(logged_in)  # Verificar que el inicio de sesión fue exitoso

    def test_login_with_nonexistent_user(self):
        # Creamos un cliente de prueba
        client = Client()

        # Intentamos iniciar sesión con un usuario inexistente
        response = client.post(reverse('login'), {'username': 'nonexistentuser', 'password': 'nonexistentpassword'})

        # Esperamos una redirección al mismo formulario de inicio de sesión
        self.assertEqual(response.status_code, 200)
