import time

from django.db import transaction
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class LiveServerTestCase(LiveServerTestCase):
    def scrap(self):
        options = Options()
        #options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        #options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
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
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        driver.execute_script("document.getElementById('changestate57-596-5887').click();")
        estado = driver.find_element(By.NAME, "estado")
        estado.clear()
        estado.send_keys("Inactivo")
        button = driver.find_element(By.CLASS_NAME, "btn-submit")
        assert "Docentes" in driver.title
        status = driver.find_element(By.NAME, "status")
        status.send_keys("inactivo")
        buttonsubmit = driver.find_element(By.ID, "submit")
        buttonsubmit.click()
        docente = driver.find_element(By.ID, "teacher57-596-5887")
        assert docente.text.__contains__("Mano")

    def test_teacher_information(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        driver.execute_script("document.getElementById('info69-399-0990').click();")
        assert "Informacion" in driver.title
        docente = driver.find_element(By.ID, "nombre69-399-0990")
        assert docente.text.__contains__("Lon")

    def test_teacher_assigned_course(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        driver.execute_script("document.getElementById('info69-399-0990').click();")
        driver.execute_script("document.getElementById('asignarcurso').click();")
        driver.execute_script("document.getElementById('cursoPM-1').click();")
        driver.execute_script("document.getElementById('button35').click();")
        assert "Docentes" in driver.title
        driver.execute_script("document.getElementById('info69-399-0990').click();")
        cursos = driver.find_element(By.ID, "curso69-399-099035")
        assert cursos.text.__contains__("NRC:35")

    def test_viatic_list(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('viaticos').click();")
        assert "Listado de Viáticos" in driver.title
        codigo = driver.find_element(By.ID, "codigo1")
        assert codigo.text.__contains__("1")

    def test_viatic_create1(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("101")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Listado de Viáticos" in driver.title

    def test_viatic_create2(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
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
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
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
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
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
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("101")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        driver.execute_script("document.getElementById('actualizar3').click();")
        assert "Actualizar viático" in driver.title
        estado = driver.find_element(By.NAME, "estado_viatico")
        estado.send_keys('aprobado')
        descripcion = driver.find_element(By.NAME, "descripcion")
        descripcion.send_keys('aprobamiento del viatico mi papa')
        presupuesto = driver.find_element(By.NAME, "presupuesto")
        presupuesto.send_keys('250000')
        guardar = driver.find_element(By.CLASS_NAME, "submit-btn")
        guardar.click()
        assert "Listado de Viáticos" in driver.title

    def test_viatic_modificar(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
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
        docente.send_keys("69-399-0990")
        clase = driver.find_element(By.NAME, "clase")
        clase.send_keys("101")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        driver.execute_script("document.getElementById('eliminar3').click();")
        assert "Eliminar viático" in driver.title
        guardar = driver.find_element(By.CLASS_NAME, "delete-button")
        guardar.click()
        assert "Listado de Viáticos" in driver.title
        
    def test_view_contract(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('contratos').click();")
        self.assertIn("Ver Contratos", self.selenium.title)
        contract_cards = self.selenium.find_elements(By.CLASS_NAME, "card")
        self.assertTrue(len(contract_cards) > 0)
        
    def test_edit_contract(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        driver.execute_script("document.getElementById('contratos').click();")
        driver.execute_script("document.getElementById('send').click();")
        self.assertIn("Editar Contrato", self.selenium.title)
        codigo_field = self.selenium.find_element(By.NAME, "txtCodigo")
        self.assertIsNotNone(codigo_field)
        fecha_elaboracion_field = self.selenium.find_element(By.NAME, "fecha_elaboracion")
        self.assertIsNotNone(fecha_elaboracion_field)
        tipo_contrato_field = self.selenium.find_element(By.NAME, "tipo_contrato")
        self.assertIsNotNone(tipo_contrato_field)
        estado_contrato_field = self.selenium.find_element(By.NAME, "estado_contrato")
        self.assertIsNotNone(estado_contrato_field)
        docente_field = self.selenium.find_element(By.NAME, "docente")
        self.assertIsNotNone(docente_field)

        




