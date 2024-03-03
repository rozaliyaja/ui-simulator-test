from selenium.webdriver.common.by import By
from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class CheckboxesAndScrollPage(BaseObject, Assertions):
    CHECKBOX_1: tuple = (By.CSS_SELECTOR, ".checkbox-list li:first-child")
    CHECKBOX_2: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(2)")
    CHECKBOX_3: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(3)")
    CHECKBOX_4: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(4)")
    CHECKBOX_5: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(5)")
    CHECKBOX_6: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(6)")
    CHECKBOX_7: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(7)")
    CHECKBOX_8: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(8)")
    CHECKBOX_9: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(9)")
    CHECKBOX_10: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(10)")
    CHECKBOX_11: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(11)")
    CHECKBOX_12: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(12)")
    CHECKBOX_13: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(13)")
    CHECKBOX_14: tuple = (By.CSS_SELECTOR, ".checkbox-list li:nth-child(14)")
    CHECKBOX_15: tuple = (By.CSS_SELECTOR, ".checkbox-list li:last-child")
    COUNT_MSG: tuple = (By.ID, "counter")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

