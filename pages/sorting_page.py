from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class GamePage(BaseObject, Assertions):
    NAME_DESC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:first-child.desc")
    NAME_ASC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:first-child.asc")
    AGE_DESC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:nth-child(2).desc")
    AGE_ASC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:nth-child(2).asc")
    ROLE_DESC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:last-child.desc")
    ROLE_ASC_FIELD: tuple = (By.CSS_SELECTOR, "#myTable th:last-child.asc")
    MAX_ATTEMPTS_FIELD: tuple = (By.ID, "maxNumber")
    START_BTN: tuple = (By.ID, "startBtn")
    BACK_BTN: tuple = (By.CLASS_NAME, "back-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)