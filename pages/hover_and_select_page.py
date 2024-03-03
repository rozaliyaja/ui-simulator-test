from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class HoverAndSelectPage(BaseObject, Assertions):
    SELECT_BTN: tuple = (By.CSS_SELECTOR, ".dropdown")
    DRAG_AND_DROP_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:first-child")
    INPUT_AND_CLICK_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:nth-child(2)")
    CHECKBOXES_AND_SCROLL_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:nth-child(3)")
    CHECK_AND_VALIDATE_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:nth-child(4)")
    SORTING_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:nth-child(5)")
    GAME_BTN: tuple = (By.CSS_SELECTOR, ".dropdown-content li:nth-child(6)")
    LOGOUT_BTN: tuple = (By.CSS_SELECTOR,".logout-button")


    def __init__(self, driver: WebDriver):
        super().__init__(driver)
