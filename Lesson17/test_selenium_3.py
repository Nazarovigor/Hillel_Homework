import allure
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@allure.story('UI Tests')
class TestSuit():

    def setup_method(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://the-internet.herokuapp.com/')
        self.browser.set_window_size(1093, 726)

    def teardown_method(self):
        self.browser.quit()

    @allure.description('notification')
    @allure.title('test_notification_message')
    @allure.severity(allure.severity_level.BLOCKER)
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
            assert message.text in ['Action successful\n×', 'Action unsuccessful, please try again\n×',
                                    'Action unsuccesful, please try again\n×']

        except NoSuchElementException:
            print(f'The element not found')

    @allure.description('broken images')
    @allure.title('test_broken_images')
    @allure.severity(allure.severity_level.CRITICAL)
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
