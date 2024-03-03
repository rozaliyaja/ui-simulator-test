from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class GamePage(BaseObject, Assertions):
    MAX_NUMBER_FIELD: tuple = (By.ID, "maxNumber")
    MAX_ATTEMPTS_FIELD: tuple = (By.ID, "maxNumber")
    START_BTN: tuple = (By.ID, "startBtn")
    BACK_BTN: tuple = (By.CLASS_NAME, "back-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)