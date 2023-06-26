from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class TestSuit():

    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://uitestingplayground.com/home')
        self.browser.set_window_size(1093, 726)

    def teardown_method(self):
        self.browser.quit()

    def test_text_input(self):
        try:
            key = 'Ivan'
            self.browser.find_element(By.CSS_SELECTOR, "[href='/textinput']").click()
            el = WebDriverWait(self.browser, timeout=3).until(lambda d: d.find_element(By.CSS_SELECTOR,
                                                                                       "[placeholder='MyButton']"))
            el.click()
            el.send_keys(key)
            button = self.browser.find_element(By.ID, "updatingButton")
            button.click()
            assert button.text == key

        except NoSuchElementException:
            print(f'The element not found')

    def test_overlapped_element(self):
        try:
            key = 'Vova'
            self.browser.find_element(By.CSS_SELECTOR, "[href='/overlapped']").click()
            target = self.browser.find_element(By.ID, "name")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", target)
            actions = ActionChains(self.browser)
            actions.move_to_element(target)
            actions.perform()
            target.click()
            target.send_keys(key)

            assert target.get_attribute("value") == key

        except NoSuchElementException:
            print(f'The element not found')