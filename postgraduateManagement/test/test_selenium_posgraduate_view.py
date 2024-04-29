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
        return driver

    def testLogin_correct(self):
        driver = self.scrap()
        driver.get('http://127.0.0.1:8000/')
        assert "Login" in driver.title
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('mrzen')
        password.send_keys('1026')
        submit.click()
        assert "Programas de Posgrado" in driver.title

    def testLogin_incorrect(self):
        driver = self.scrap()
        driver.get('http://127.0.0.1:8000/')
        assert "Login" in driver.title
        username = driver.find_element(By.NAME, "username")
        password = driver.find_element(By.NAME, "password")
        submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        username.send_keys('abdulab')
        password.send_keys('the meaning of the life is the 42')
        submit.click()
        assert "Login" in driver.title
