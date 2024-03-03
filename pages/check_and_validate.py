from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class CheckAndValidatePage(BaseObject, Assertions):
    VALUE_FIELD: tuple = (By.ID, "dataInput")
    CHECK_MSG: tuple = (By.ID, "validationSquare")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def enter_value(self, value):
        self.send_keys(self.VALUE_FIELD, value)

    def check_message(self, msg):
        self.assert_equal(actual=self.get_text(self.CHECK_MSG), expected=msg)
