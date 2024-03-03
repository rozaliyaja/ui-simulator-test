from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class InputAndClickPage(BaseObject, Assertions):
    DATA_FIELD: tuple = (By.ID, "inputText")
    ADD_BTN: tuple = (By.ID, "addBtn")
    DELETE_BTN: tuple = (By.ID, "deleteBtn")
    ITEM_FIELD: tuple = (By.CLASS_NAME, "item")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('entering item to data field')
    def enter_data(self, item):
        self.send_keys(self.DATA_FIELD, item)

    @allure.step('click to add button')
    def click_add_button(self):
        self.click(self.ADD_BTN)

    @allure.step('check item field is invisible')
    def check_item_fields_is_invisible(self):
        self.assert_boolean(actual=self._is_invisible(self.ITEM_FIELD))
         # selfassert_boolean(actual=self._is_invisible(self.ITEM_FIELD), ex))
        # ДЗ Как протестировать assert boolean

    @allure.step('click to delete button')
    def click_delete_button(self):
        self.click(self.DELETE_BTN)

    def check_data_on_item_field(self, item):
        self.assert_equal(actual=self.get_text(self.ITEM_FIELD), expected=item)
