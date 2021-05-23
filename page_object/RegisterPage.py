from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from page_object.FindAndClick import FindAndClick


class RegisterPage(FindAndClick):

    def _add_information(self, first_name, last_name, email, tel, password):
        time.sleep(5)
        self._verify_id_presence("input-firstname").send_keys(first_name)
        self._verify_id_presence("input-lastname").send_keys(last_name)
        self._verify_id_presence("input-email").send_keys(email)
        self._verify_id_presence("input-telephone").send_keys(tel)
        self._verify_id_presence("input-password").send_keys(password)
        self._verify_id_presence("input-confirm").send_keys(password)
        self._name("agree")
        self._class_name("btn-primary")