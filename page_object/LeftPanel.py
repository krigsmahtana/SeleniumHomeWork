from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from page_object.FindAndClick import FindAndClick


class LefPanel(FindAndClick):

    def catalog(self, point):
        self._id("menu-catalog")
        self._xpath("//*[@id='collapse1']/li[2]")


