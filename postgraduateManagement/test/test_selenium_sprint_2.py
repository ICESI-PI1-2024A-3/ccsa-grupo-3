import time

from django.db import transaction
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager



class LiveServerTestCase(LiveServerTestCase):
    def scrap(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        #driver.get('http://127.0.0.1:8000/')
        driver.get('https://ccsa-modulo-programacion-academica.onrender.com')
        return driver

    def test_home_links(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        assert "Programas de Posgrado" in driver.title
        driver.back()
        driver.execute_script("document.getElementById('docentes').click();")
        assert "Docentes" in driver.title
        driver.back()
        driver.execute_script("document.getElementById('contratos').click();")
        assert "Contratos" in driver.title
        driver.back()

    def test_change_state_teacher(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        driver.execute_script("document.getElementById('changestate81-573-3242').click();")
        assert "Editar Estado del Docente" in driver.title
        estado = driver.find_element(By.ID, "id_estado")
        estado.send_keys("inactivo")
        button = driver.find_element(By.CLASS_NAME, "btn-submit")
        button.click()
        assert "Docentes" in driver.title
        status = driver.find_element(By.NAME, "status")
        status.send_keys("inactivo")
        buttonsubmit = driver.find_element(By.ID, "submit")
        buttonsubmit.click()
        docente = driver.find_element(By.ID, "name81-573-3242")
        assert docente.text.__contains__("Lilias Kennham")

    def test_teacher_information(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        driver.execute_script("document.getElementById('info81-573-3242').click();")
        assert "Información" in driver.title
        docente = driver.find_element(By.ID, "nombre81-573-3242")
        assert docente.text.__contains__("Lilias")

    def test_viatic_list(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        assert "Listado de Viáticos" in driver.title
        codigo = driver.find_element(By.ID, "codigo4")
        assert codigo.text.__contains__("4")

    def test_viatic_create1_and_eliminate(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        driver.execute_script("document.getElementById('crear').click();")
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('pendiente')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('viatico')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('25000')
        docente = driver.find_element(By.NAME, "docente")
        docente.send_keys("60-190-1250")
        clase = driver.find_element(By.NAME, "clase")
        select = Select(clase)
        select.select_by_value("101")
        guardar = driver.find_element(By.ID, "guardar")
        guardar.click()
        assert "Listado de Viáticos" in driver.title
        driver.execute_script("document.getElementById('eliminarviatico').click();")
        assert "Eliminar viático" in driver.title
        guardar = driver.find_element(By.ID, "delete")
        guardar.click()
        assert "Listado de Viáticos" in driver.title

    def test_viatic_create2(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        driver.execute_script("document.getElementById('crear').click();")
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('aprobado')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('viatico')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('-250')
        docente = driver.find_element(By.NAME, "docente")
        docente.send_keys("60-190-1250")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("202")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear viático" in driver.title

    def test_viatic_create3(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        driver.execute_script("document.getElementById('crear').click();")
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('rechazado')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('viatico')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('-250')
        docente = driver.find_element(By.NAME, "docente")
        docente.send_keys("60-190-1250")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("101")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear viático" in driver.title

    def test_viatic_create4(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        driver.execute_script("document.getElementById('crear').click();")
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('rechazado')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('viatico')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('150')
        docente = driver.find_element(By.NAME, "docente")
        docente.send_keys("60-190-1250")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("0")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear viático" in driver.title

    def test_viatic_modificar(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        driver.execute_script("document.getElementById('actualizar4').click();")
        assert "Actualizar viático" in driver.title
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('aprobado')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('aprobamiento  viatico mi papa')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('250000')
        guardar = driver.find_element(By.CLASS_NAME, "submit-btn")
        guardar.click()
        assert "Listado de Viáticos" in driver.title
        # reseteo pre prueba
        driver.execute_script("document.getElementById('actualizar4').click();")
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('pendiente')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('dd')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('100')
        guardar = driver.find_element(By.CLASS_NAME, "submit-btn")
        guardar.click()

    def test_contracts(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('contratos').click();")
        assert "Contratos" in driver.title

    def test_contracts2(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('contratos').click();")
        assert "Contratos" in driver.title
        driver.execute_script("document.getElementById('send').click();")
        assert "Editar Contrato" in driver.title

    def test_contracts3(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('contratos').click();")
        assert "Contratos" in driver.title
        driver.execute_script("document.getElementById('send').click();")
        assert "Editar Contrato" in driver.title
        fecha_elaboracion_input = driver.find_element(By.NAME, 'fecha_elaboracion')
        fecha_elaboracion_input.send_keys('2024-05-20')
        tipo_contrato_select = driver.find_element(By.ID, 'tipo_contrato')
        tipo_contrato_select.send_keys('Tiempo parcial')
        estado_contrato_select = driver.find_element(By.ID, 'estado_contrato')
        estado_contrato_select.send_keys('Vencido')
        driver.execute_script("document.getElementById('send2').click();")
        assert driver.current_url.__contains__("editingContract")




        




