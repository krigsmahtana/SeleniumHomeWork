import pytest
import allure
import os

from selenium import webdriver

DRIVERS = "C:/Users/Vasileva_I/Documents/SeleniumDrivers"
rootdir = "C:/Users/Vasileva_I/Documents/курсы/OTUS Pyton/SeleniumHomeWork"

def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")
    parser.addoption("--url", "-U", default="http://localhost/")


@allure.step('step in conftest.py')
def conftest_step():
    pass


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    url = request.config.getoption("--url")

    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")

    request.addfinalizer(driver.quit)

    def open(path=""):
        return driver.get(url + path)

    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.open = open
    driver.open()

    return driver


@pytest.fixture(scope="session")
def get_environment(pytestconfig):
    props = {
        'Shell': os.getenv('SHELL'),
        'Terminal': os.getenv('TERM'),
        'Stand': 'Production'
    }

    tests_root = pytestconfig.rootdir
    with open(f'{tests_root}/allure-results/environment.properties', 'w') as f:
        for k, v in props.items():
            f.write(f'{k}={v}\n')
