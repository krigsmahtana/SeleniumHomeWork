import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from page_object.FindAndClick import FindAndClick
from page_object.AdminPage import AdminLoginForm
from page_object.AdminProduct import AdminProduct
from page_object.LeftPanel import LefPanel
from page_object.RegisterPage import RegisterPage
from page_object.TopMenu import TopMenu
from page_object.SearchPage import SearchPage
from page_object.LoginPage import LoginPage
import allure


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Open page Cameras")
def test_one_page(browser):
    try:
        wait = WebDriverWait(browser, 30)
        wait.until(EC.title_is("Your Store"))
        WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.ID, "menu")))
        FindAndClick(browser)._xpath("//*[@id='menu']/div[2]/ul/li[7]/a")
        name_page = FindAndClick(browser)._verify_css_presence("#content > h2").text
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert name_page == "Cameras"
        col = browser.find_element_by_css_selector("#content > div:nth-child(3)").text
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert col != "ll"
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.title("Open page Desktops")
def test_two_page(browser):
    try:
        browser.find_elements_by_link_text("Desktops")[0].click()
        FindAndClick(browser)._class_name("see-all")
        wait = WebDriverWait(browser, 30)
        wait.until(EC.title_is("Desktops"))
        FindAndClick(browser)._id("list-view")
        FindAndClick(browser)._id("grid-view")
        browser.find_element_by_name("search").send_keys("test")
        FindAndClick(browser)._css("#search > span > button")
        answer = browser.find_element_by_css_selector("#content > h2").text
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert answer == "Products meeting the search criteria"
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.title("Finde product Samsung Galaxy Tab")
def test_three_page(browser):
    try:
        TopMenu(browser).find_product("Samsung Galaxy Tab")
        SearchPage(browser).click_in_find_product("Samsung Galaxy Tab")
        wait = WebDriverWait(browser, 30)
        wait.until(EC.title_is("Samsung Galaxy Tab 10.1"))
        price = browser.find_element_by_css_selector("#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > "
                                                     "h2").text
        assert price == "$241.99"
        tax = browser.find_element_by_css_selector("#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(2)").text
        assert tax == "Ex Tax: $199.99"
        browser.find_element_by_name("quantity").send_keys("2")
        FindAndClick(browser)._id("button-cart")
        alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
        alert = alert.text
        assert alert == "Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!\n×"
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.title("Open Account Login")
def test_four_page(browser):
    try:
        TopMenu(browser).login()
        wait = WebDriverWait(browser, 20)
        wait.until(EC.title_is("Account Login"))
        LoginPage(browser)._login("user1", "user")
        alert = browser.find_element_by_class_name("alert").text
        assert alert == "Warning: No match for E-Mail Address and/or Password."
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.feature('Open Admin page like admin')
@pytest.mark.parametrize("url", ["http://localhost/"])
def test_five_page(browser, url):
    try:
        browser.get(url + "/admin/")
        wait = WebDriverWait(browser, 20)
        wait.until(EC.title_is("Administration"))
        AdminLoginForm(browser).userloginform("user", "bitnami")
        browser.find_element_by_id("user-profile")
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.feature('ADD new product')
@pytest.mark.parametrize("url", ["http://localhost/"])
def test_add_new_product(browser, url):
    try:
        browser.get(url + "/admin/")
        wait = WebDriverWait(browser, 20)
        wait.until(EC.title_is("Administration"))
        AdminLoginForm(browser).userloginform("user", "bitnami")
        LefPanel(browser).catalog("Products")
        AdminProduct(browser).add_new_product("testName", "TT", "TT")
        AdminProduct(browser).find_product("testName")
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.feature('DELETE new product')
@pytest.mark.parametrize("url", ["http://localhost/"])
def test_delet_product(browser, url):
    try:
        browser.get(url + "/admin/")
        wait = WebDriverWait(browser, 20)
        wait.until(EC.title_is("Administration"))
        AdminLoginForm(browser).userloginform("user", "bitnami")
        LefPanel(browser).catalog("Products")
        AdminProduct(browser).delete_product("testName")
        browser.switch_to_alert().accept()
        browser.find_element_by_class_name("alert-dismissible")
        browser.quit()
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.severity(allure.severity_level.TRIVIAL)
@allure.feature('Change currency')
def test_change_currency(browser):
    try:
        pytest.skip('Пропуская для отображение в отчете')
        TopMenu(browser).change_currency("EUR")
        browser.find_elements_by_link_text("£")
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    except:
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        raise Exception('inna-test-failed')


@allure.severity(allure.severity_level.BLOCKER)
@allure.feature('Created account')
def test_new_user(browser):
    with allure.step('Test Created account'):
        try:
            TopMenu(browser).register()
            RegisterPage(browser)._add_information("NameTest", "Famely", "test4@test.test", "1234", "1234")
            time.sleep(10)
            text = FindAndClick(browser)._verify_css_presence("#content > h1").text
            assert text == "Your Account Has Been Created!"
            FindAndClick(browser)._class_name("pull-right")
        except:
            allure.attach(browser.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
            raise Exception('inna-test-failed')
