import pytest
import os

from selenium import webdriver

DRIVERS = "C:/Users/Vasileva_I/Documents/SeleniumDrivers"


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", choices=["chrome", "firefox", "opera"], default="chrome")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")

    driver = None

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver")
    elif browser == "opera":
        driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver")

    request.addfinalizer(driver.quit)

    if maximized:
        driver.maximize_window()

    return driver
