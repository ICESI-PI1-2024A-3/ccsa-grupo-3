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
        #driver.get('https://ccsa-modulo-programacion-academica.onrender.com')
        return driver

    def test_Login_correct(self):
        driver = self.scrap()
        assert "Login" in driver.title
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        assert "Inicio" in driver.title

    def test_Login_incorrect(self):
        driver = self.scrap()
        assert "Login" in driver.title
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('abdulab')
        password.send_keys('the meaning of the life is the 42')
        submit.click()
        assert "Login" in driver.title

    def test_Program_view_normal_interaction(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        assert "Programas de Posgrado" in driver.title
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        assert driver.find_element(By.ID, "wrapperInfo")
        driver.execute_script("document.getElementById('programation').click();")
        assert "Programa: Maestría en Educación | Universidad Icesi" in driver.title

    def test_SubjectList_interaction(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        assert driver.find_element(By.ID, "PM-1")
        assert driver.find_element(By.ID, "PM-22")
        driver.execute_script("document.getElementById('PM-1').click();")
        assert "Listado de Cursos" in driver.title

    def test_Courses_List_interaction(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-1').click();")
        assert driver.find_element(By.ID, "nrc123123")
        assert driver.find_element(By.ID, "grupo1231236")
        nrc = driver.find_element(By.ID, "nrc123123")
        grupo = driver.find_element(By.ID, "grupo1231236")
        assert nrc.text == "123123"
        assert grupo.text == "6"
        driver.execute_script("document.getElementById('delete123123').click();")
        assert "Eliminar curso" in driver.title
        driver.back()
        driver.execute_script("document.getElementById('update123123').click();")
        assert "Editar Curso" in driver.title
        driver.back()
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title

    def test_Course_create1(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('0')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('0')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('-10')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title

    def test_Course_create2(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('50')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('50')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('25')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Listado de Cursos" in driver.title
        # desde aqui se hace un proceso de limpieza de la db
        driver.execute_script("document.getElementById('delete50').click();")
        driver.execute_script("document.getElementById('delete').click();")

    def test_Course_create3(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('999999')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('99')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('100')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title

    def test_Course_create4(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('0')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('50')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('100')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title
        # desde aqui se hace un proceso de limpieza de la db

    def test_Course_create5(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('50')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('0')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('100')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title

    def test_Course_create6(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('999999')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('0')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('25')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Listado de Cursos" in driver.title
        # desde aqui se hace un proceso de limpieza de la db
        driver.execute_script("document.getElementById('delete999999').click();")
        driver.execute_script("document.getElementById('delete').click();")

    def test_Course_create7(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('0')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('99')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('25')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Listado de Cursos" in driver.title
        # desde aqui se hace un proceso de limpieza de la db
        driver.execute_script("document.getElementById('delete0').click();")
        driver.execute_script("document.getElementById('delete').click();")

    def test_Course_create8(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('50')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('99')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('-10')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title

    def test_Course_create9(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        assert "Crear curso" in driver.title
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('999999')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('50')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('-10')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        assert "Crear curso" in driver.title

    def test_modify_course(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('50')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('50')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('25')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        driver.execute_script("document.getElementById('update50').click();")
        assert "Editar Curso" in driver.title
        assert driver.find_element(By.NAME, "grupo")
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.clear()
        grupo.send_keys('65')
        assert driver.find_element(By.NAME, "cupo")
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.clear()
        cupo.send_keys('70')
        assert driver.find_element(By.CLASS_NAME, "submit-btn")
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "submit-btn")
        guardar.click()
        assert "Listado de Cursos" in driver.title
        assert driver.find_element(By.ID, "nrc50")
        assert driver.find_element(By.ID, "grupo5065")
        nrc = driver.find_element(By.ID, "nrc50")
        grupo11 = driver.find_element(By.ID, "grupo5065")
        assert nrc.text == "50"
        assert grupo11.text == "65"
        # desde aqui se hace un proceso de limpieza de la db
        driver.execute_script("document.getElementById('delete50').click();")
        driver.execute_script("document.getElementById('delete').click();")

    def test_delete_course(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        principalprogram = driver.find_element(By.ID, "buttonPROG002-M")
        principalprogram.click()
        driver.execute_script("document.getElementById('programation').click();")
        driver.execute_script("document.getElementById('subjects').click();")
        driver.execute_script("document.getElementById('PM-5').click();")
        driver.execute_script("document.getElementById('createbutton').click();")
        nrc = driver.find_element(By.NAME, "nrc")
        nrc.send_keys('50')
        grupo = driver.find_element(By.NAME, "grupo")
        grupo.send_keys('50')
        cupo = driver.find_element(By.NAME, "cupo")
        cupo.send_keys('25')
        periodo = driver.find_element(By.NAME, "periodo")
        periodo.send_keys("1")
        guardar = driver.find_element(By.CLASS_NAME, "btn-submit")
        guardar.click()
        driver.execute_script("document.getElementById('delete50').click();")
        assert "Eliminar curso" in driver.title
        driver.execute_script("document.getElementById('delete').click();")
        assert "Listado de Cursos" in driver.title

    def test_nav_bar_references(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('programas').click();")
        driver.execute_script("document.getElementById('home').click();")
        # cambiar el home con el home nuevo obvio
        assert "Inicio" in driver.title
        driver.execute_script("document.getElementById('programas').click();")
        # programa de la nav bar
        driver.execute_script("document.getElementById('programas').click();")
        assert "Programas de Posgrado" in driver.title
        driver.execute_script("document.getElementById('teacher').click();")
        assert "Docentes" in driver.title
        driver.execute_script("document.getElementById('viaticos').click();")
        assert "Listado de Viáticos" in driver.title

    def test_teacher_search_by_name(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        search = driver.find_element(By.NAME, "search_contains")
        search.send_keys("Lotte")
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        docente = driver.find_element(By.ID, "name60-190-1250")
        assert docente.text.__contains__("Lotte")

    def test_teacher_search_by_state_inactive(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        search = driver.find_element(By.NAME, "status")
        search.send_keys("inactivo")
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        docente = driver.find_element(By.ID, "name60-190-1250")
        assert docente.text.__contains__("Lotte")

    def test_teacher_search_by_state_active(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        search = driver.find_element(By.NAME, "status")
        search.send_keys("activo")
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        docente = driver.find_element(By.ID, "name17-648-5695")
        assert docente.text.__contains__("Querida Medlen")

    def test_teacher_search_by_city(self):
        driver = self.scrap()
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys(' miguel.angel@icesi.edu.co')
        password.send_keys('contraseña')
        submit.click()
        driver.execute_script("document.getElementById('docentes').click();")
        search = driver.find_element(By.NAME, "city")
        search.send_keys("1")
        submit = driver.find_element(By.ID, "submit")
        submit.click()
        docente = driver.find_element(By.ID, "name17-648-5695")
        assert docente.text.__contains__("Querida Medlen")
