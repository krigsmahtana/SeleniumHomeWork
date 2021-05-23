from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindAndClick:
    def __init__(self, browser):
        self.browser = browser

    def _verify_id_presence(self, id):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.ID, id)))
        except TimeoutException:
            raise AssertionError("Cant find element by id:{}".format(id))

    def _verify_name_presence(self, name):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.NAME, name)))
        except TimeoutException:
            raise AssertionError("Cant find element by name:{}".format(name))

    def _verify_css_presence(self, css):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css)))
        except TimeoutException:
            raise AssertionError("Cant find element by css:{}".format(css))

    def _verify_xpath_presence(self, xpath):
        try:
            return WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise AssertionError("Cant find element by xpath:{}".format(xpath))

    def _verify_class_name_presence(self, class_name):
        try:
            return WebDriverWait(self.browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, class_name)))
        except TimeoutException:
            raise AssertionError("Cant find element by class_name:{}".format(class_name))

    def _id(self, id):
        self._verify_id_presence(id).click()

    def _name(self, name):
        self._verify_name_presence(name).click()

    def _css(self, css):
        self._verify_css_presence(css).click()

    def _xpath(self, xpath):
        self._verify_xpath_presence(xpath).click()

    def _class_name(self, class_name):
        self._verify_class_name_presence(class_name).click()