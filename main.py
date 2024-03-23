import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def Get_Site():
    driver.get("https://demo-opencart.ru/")


def test_images_product():
    Get_Site()
    time.sleep(2)
    product_link = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-12 div.row:nth-child(4) div.product-layout.col-lg-3.col-md-3.col-sm-6.col-xs-12:nth-child(1) div.product-thumb.transition div.image a:nth-child(1) > img.img-responsive")
    product_link.click()
    time.sleep(4)

    thumbnails = driver.find_element(By.CSS_SELECTOR,  "div.container:nth-child(4) div.row div.col-sm-12 div.row div.col-sm-8 ul.thumbnails li:nth-child(1) a.thumbnail > img:nth-child(1)")
    thumbnails.click()
    time.sleep(2)

    list_Prod = driver.find_element(By.CSS_SELECTOR, "body:nth-child(2) div.mfp-wrap.mfp-gallery.mfp-close-btn-in.mfp-auto-cursor.mfp-ready:nth-child(2) div.mfp-container.mfp-s-ready.mfp-image-holder > button.mfp-arrow.mfp-arrow-right.mfp-prevent-close:nth-child(4)")
    for i in range(4):
        list_Prod.click()
        time.sleep(2)


def test_korzina():
    Get_Site()

    time.sleep(2)
    korzina_catalog_lik = driver.find_element(By.CSS_SELECTOR, "#top-links > ul > li:nth-child(4) > a > i")
    korzina_catalog_lik.click()
    time.sleep(2)
    try:
        summ = driver.find_element(By.CSS_SELECTOR, "#content > div.row > div > table > tbody > tr:nth-child(2) > td:nth-child(2)")
        if summ > 0:
            print("Товар в корзине")
    except:
        print("Корзина пуста")


def test_empty_category():

    Get_Site()

    search = driver.find_element(By.CSS_SELECTOR,"div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) > a.dropdown-toggle")
    search.click()
    time.sleep(2)

    search = driver.find_element(By.CSS_SELECTOR,"div.container:nth-child(3) nav.navbar div.collapse.navbar-collapse.navbar-ex1-collapse ul.nav.navbar-nav li.dropdown:nth-child(1) div.dropdown-menu div.dropdown-inner ul.list-unstyled li:nth-child(1) > a:nth-child(1)")
    search.click()
    time.sleep(2)

    products = driver.find_elements(By.CSS_SELECTOR, ".product-layout")
    if not products:
        print("Страница категории PC пуста.")
    else:
        print("Страница категории PC не пуста.")


def test_registration():
    Get_Site()
    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown:nth-child(2) > "
                                 "a.dropdown-toggle")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR,
                                 "div.container div.nav.pull-right ul.list-inline li.dropdown.open:nth-child(2) "
                                 "ul.dropdown-menu.dropdown-menu-right li:nth-child(1) > a:nth-child(1)")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-firstname")
    words = "Саторо"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-lastname")
    words = "Годжо"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-email")
    words = "Gojo@gmail.com"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-telephone")
    words = "89998887766"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-password")
    words = "Gojo1"
    search.click()
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "#input-confirm")
    words = "Gojo1"
    for letter in words:
        search.send_keys(letter)
    time.sleep(2)
    search.click()

    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input:nth-child(3)")
    search.click()
    time.sleep(2)
    search = driver.find_element(By.CSS_SELECTOR, "div.container:nth-child(4) div.row div.col-sm-9 form.form-horizontal:nth-child(3) div.buttons:nth-child(4) div.pull-right > input.btn.btn-primary:nth-child(4)")
    search.click()
    time.sleep(2)


def test_poisk():
    Get_Site()
    time.sleep(2)
    search_input = driver.find_element(By.NAME, "search")
    search_input.click()
    words = "Gojo"
    for letter in words:
        search_input.send_keys(letter)
    time.sleep(2)
    search_button = driver.find_element(By.CSS_SELECTOR, "div.container div.row div.col-sm-5 div.input-group span.input-group-btn button.btn.btn-default.btn-lg > i.fa.fa-search")
    search_button.click()
    time.sleep(2)


test_images_product()
test_korzina()
test_empty_category()
test_registration()
test_poisk()


driver.quit()
