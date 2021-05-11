import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize("url", ["http://localhost/"])
def test_one_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 30)
    wait.until(EC.title_is("Your Store"))
    WebDriverWait(browser, 7).until(EC.visibility_of_element_located((By.ID, "menu")))
    browser.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[7]/a").click()
    name_page = browser.find_element_by_css_selector("#content > h2").text
    assert name_page == "Cameras"
    col = browser.find_element_by_css_selector("#content > div:nth-child(3)").text
    assert col != "ll"
    browser.quit()


@pytest.mark.parametrize("url", ["http://localhost/"])
def test_two_page(browser, url):
    browser.get(url + "index.php?route=product/category&path=20")
    wait = WebDriverWait(browser, 30)
    wait.until(EC.title_is("Desktops"))
    browser.find_element_by_id("list-view").click()
    browser.find_element_by_id("grid-view").click()
    browser.find_element_by_name("search").send_keys("test")
    browser.find_element_by_css_selector("#search > span > button").click()
    answer = browser.find_element_by_css_selector("#content > h2").text
    assert answer == "Products meeting the search criteria"
    browser.quit()


@pytest.mark.parametrize("url", ["http://localhost/"])
def test_three_page(browser, url):
    browser.get(url + "/index.php?route=product/product&path=57&product_id=49")
    wait = WebDriverWait(browser, 30)
    wait.until(EC.title_is("Samsung Galaxy Tab 10.1"))
    price = browser.find_element_by_css_selector("#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(1) > "
                                                 "h2").text
    assert price == "$241.99"
    tax = browser.find_element_by_css_selector("#content > div > div.col-sm-4 > ul:nth-child(4) > li:nth-child(2)").text
    assert tax == "Ex Tax: $199.99"
    browser.find_element_by_name("quantity").send_keys("2")
    browser.find_element_by_id("button-cart").click()
    alert = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
    alert = alert.text
    assert alert == "Success: You have added Samsung Galaxy Tab 10.1 to your shopping cart!\n×"
    browser.quit()


@pytest.mark.parametrize("url", ["http://localhost/"])
def test_four_page(browser, url):
    browser.get(url + "/index.php?route=account/login")
    wait = WebDriverWait(browser, 20)
    wait.until(EC.title_is("Account Login"))
    browser.find_element(By.NAME, "email").send_keys("user1")
    browser.find_element(By.NAME, "password").send_keys("user")
    browser.find_element_by_xpath("//*[@id='content']/div/div[2]/div/form/input").click()
    alert = browser.find_element_by_class_name("alert").text
    assert alert == "Warning: No match for E-Mail Address and/or Password."
    browser.quit()


@pytest.mark.parametrize("url", ["http://localhost/"])
def test_five_page(browser, url):
    browser.get(url + "/admin/")
    wait = WebDriverWait(browser, 20)
    wait.until(EC.title_is("Administration"))
    browser.find_element(By.NAME, "username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element_by_css_selector("#content > div > div > div > div > div.panel-body > form > div.text-right > "
                                         "button").click()
    browser.find_element_by_id("user-profile")
    browser.quit()