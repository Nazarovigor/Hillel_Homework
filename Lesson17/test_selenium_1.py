from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class TestUi():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
        self.driver.set_window_size(1093, 726)

    def teardown_method(self):
        self.driver.quit()

    def test_home_button_is_present(self):

        try:
            el = WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR, '.btn.home'))
            assert el.text == "Home"
        except NoSuchElementException:
            print(f'The element not found')

    def test_customer_login_button_is_present(self):

        try:
            el2 = WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR,
                                                                                       ".center [ng-click='customer()']"))
            assert el2.text == "Customer Login"
        except NoSuchElementException:
            print(f'The element not found')

    def test_bank_manager_ligin_button_is_present(self):

        try:
            el3 = WebDriverWait(self.driver, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR,
                                                                                       '.center:last-child'))
            assert el3.text == "Bank Manager Login"
        except NoSuchElementException:
            print(f'The element not found')


