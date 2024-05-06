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
        service = Service(ChromeDriverManager().install())
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(options=options)
        driver.get('http://127.0.0.1:8000/')
        return driver

    def test_home_links(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
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



