from selenium.webdriver.common.by import By


def test_basket_button(driver):
    driver.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    assert len(driver.find_elements(By.CLASS_NAME, "btn-add-to-basket")) != 0, "Кнопка отсутствует"
