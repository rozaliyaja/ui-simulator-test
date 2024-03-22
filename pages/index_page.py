from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class IndexPage(BaseObject, Assertions):
    USERNAME_FIELD: tuple = (By.ID, "username")
    PASSWORD_FIELD: tuple = (By.ID, "password")
    LOGIN_BTN: tuple = (By.CLASS_NAME, "login-button")
    ERROR_MSG: tuple = (By.CLASS_NAME, "error-message")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("entering username")
    def enter_username(self, user_name):
        self.send_keys(self.USERNAME_FIELD, user_name)

    @allure.step("entering password")
    def enter_password(self, password):
        self.send_keys(self.PASSWORD_FIELD, password)

    @allure.step("click to login button")
    def click_to_login_button(self):
        self.click(self.LOGIN_BTN)

    @allure.step("comparing the expected url with the current url")
    def check_url(self):
        self.assert_equal(actual=self.get_current_url(),
                          expected='https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html')

    @allure.step("comparing the expected error message with the current error message ")
    def check_error_message(self, error_msg):
        self.assert_equal(actual=self.get_text(self.ERROR_MSG),
                          expected= error_msg)

    def clicking_by_enter_instead_of_click(self):
        self.clicking_enter(self.LOGIN_BTN)

    def check_login_btn_element_color(self, color):
        self.assert_equal(actual=self.get_element_color(self.LOGIN_BTN),
                          expected=color)
