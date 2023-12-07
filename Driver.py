from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from utils.confimration import *
from selenium.webdriver.support import expected_conditions as EC


class Driver:
    chrome_options = None
    svc = None
    driver = None
    _instance = None

    def __new__(cls, driver_path: str, proxy_adress: str):

        if cls._instance is None:
            """"Argumenty dla drivera"""
            cls._instance = super().__new__(cls)
            cls.proxy = {
                "http": f'http://{proxy_adress}',
                "https": f'https://{proxy_adress}'
            }

            cls.chrome_options = webdriver.ChromeOptions()
            cls.chrome_options.add_argument("--proxy-server={proxy['https']}")
            cls.chrome_options.add_argument("--disable-images")
            cls.chrome_options.add_argument("--no-headless")

            cls.svc = webdriver.ChromeService(executable_path=driver_path)
            cls.driver = webdriver.Chrome(options=cls.chrome_options,
                                          service=cls.svc)
        return cls._instance

    def log_in(self, login_input, login: str, password_input, password: str):
        try:
            insert_login = WebDriverWait(self.driver, 15).until(self.driver.find_element(By.XPATH, login_input))
            insert_login.send_keys(login)
            insert_password = WebDriverWait(self.driver, 15).until(self.driver.find_element(By.XPATH, password_input))
            insert_password.send_keys(password)
        except ElementNotVisibleException:
            return "Element nie został znaleziony w czasie {} sekund".format("15")

    def get_user_page(self, user_name):
        url = f"https://www.instagram.com/{user_name}/"
        self.driver.get(url)

    def search_and_click(self, element):
        try:
            WebDriverWait(self.driver, 15).until(self.driver.find_element(By.XPATH, element))
            element.click()
        except ElementNotVisibleException:
            return "Element nie został znaleziony w czasie {} sekund".format("15")

    def input_search(self, element, data):
        try:
            input_element = WebDriverWait(self.driver, 15).until(self.driver.find_element(By.XPATH, element))
            input_element.send_keys(data)
            input_element.send_keys(Keys.ENTER)
        except ElementNotVisibleException:
            return "Element nie został znaleziony w czasie {} sekund".format("15")

    def refresh_page(self):
        self.driver.refresh()

    def double_click(self, element):
        action_chains = ActionChains(self.driver)
        action_chains.double_click(element).perform()

    def check_report_sending(self, report_message=confirmation_text):
        element = self.driver.find_element(By.XPATH, f"//*[contains(text(), '{report_message}')]")
        if report_message in element.text:
            print("Report has been sent")
            self.driver.quit()
        else:
            print("Could not send report")
            self.driver.quit()
