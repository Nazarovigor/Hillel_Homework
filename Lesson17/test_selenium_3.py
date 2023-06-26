import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestSuit():

    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://the-internet.herokuapp.com/')
        self.browser.set_window_size(1093, 726)

    def teardown_method(self):
        self.browser.quit()

    def test_notification_message(self):
        try:
            target = self.browser.find_element(By.CSS_SELECTOR, "[href='/notification_message']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", target)
            actions = ActionChains(self.browser)
            actions.move_to_element(target)
            actions.perform()
            target.click()
            self.browser.find_element(By.CSS_SELECTOR, "[href='/notification_message']").click()
            message = self.browser.find_element(By.CSS_SELECTOR, '#flash.flash.notice')
            assert message.text.strip() in ['Action successful\n×', 'Action unsuccessful, please try again\n×']

        except NoSuchElementException:
            print(f'The element not found')

    def test_broken_images(self):
        try:
            broken_pic = []
            target = self.browser.find_element(By.CSS_SELECTOR, "[href='/broken_images']")
            self.browser.execute_script("arguments[0].scrollIntoView(true);", target)
            actions = ActionChains(self.browser)
            actions.move_to_element(target)
            actions.perform()
            target.click()
            pictures = self.browser.find_elements(By.TAG_NAME, "img")
            for picture in pictures:
                src = picture.get_attribute("src")
                response = requests.get(src)
                if response.status_code != 200:
                    broken_pic.append(picture)
            assert len(broken_pic) == 2

        except NoSuchElementException:
            print(f'The element not found')