from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class DragAndDropPage(BaseObject, Assertions):
    FIRST_T_BTN: tuple = (By.ID, "item-3")
    E_BTN: tuple = (By.ID, "item-2")
    S_BTN: tuple = (By.ID, "item-7")
    SECOND_T_BTN: tuple = (By.ID, "item-4")
    I_BTN: tuple = (By.ID, "item-1")
    N_BTN: tuple = (By.ID, "item-6")
    G_BTN: tuple = (By.ID,"item-5")
    DONE_MSG: tuple = (By.CSS_SELECTOR, ".done")
    BACK_BTN: tuple = (By.CSS_SELECTOR, ".back-button")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)