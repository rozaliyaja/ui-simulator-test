from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from support.logger import log_func
from selenium.webdriver import ActionChains


class BaseObject:
    LOG = log_func()

    def __init__(self, driver: WebDriver) -> object:
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    # def _is_visible(self, locator) -> WebElement:
    #     """
    #     Проверяет, что элемент видимый
    #     :param locator: элемент
    #     :return:
    #     """
    #     self.LOG.info(f'element {locator} is visible')
    #     return self.wait.until(ec.visibility_of_element_located(locator))
    #

    def _is_visible(self, locator) -> WebElement:
        """
        Проверяет, что элемент видимый
        :param locator: элемент
        :return:
        """

        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.LOG.info(f'element {locator} is visible')
            return element
        except TimeoutException:
            self.LOG.error(f'element {locator} is not visible')
        raise Exception(f'element {locator} is visible')

    def _is_invisible(self, locator: object) -> WebElement:
        """
        Проверяет, что элемент не видимый
        :param locator: элемент
        :return:
        """
        self.LOG.info(f'element {locator} is invisible')
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def _is_clickable(self, locator) -> WebElement:
        """
        Дожидается кликабельности элемента
        :param locator: элемент
        :return:
        """
        self.LOG.info(f'element {locator} is clickable')
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        """
        Кликает по элементу
        :param locator: элемент
        :return:
        """
        self.LOG.info(f'click on element {locator}')
        self._is_clickable(locator).click()

    def send_keys(self, locator: object, data: object) -> object:
        """
        Находит элемент и вводит заданный текст
        :param locator: элемент
        :param data: текст
        :return:
        """
        self.LOG.info(f'the key {data} has been sent to the element {locator}')
        self._is_visible(locator).send_keys(data)

    def get_current_url(self):
        """
        Функия возвращает url
        :return: url
        """
        self.LOG.info('the current URL was received')
        return self.driver.current_url

    def get_text(self, locator):
        """
        Элемент должен вернуть текст
        :param locator: путь до элемента, который содержит текст
        :return: текст
        """
        self.LOG.info(f'the text from the element {locator} was retrieved')
        return self._is_visible(locator).text

    # hover and drag&drop
    # doc string- 3 двойных кавычки(pycharm). Написать для base object
    # создать телеграмм бота(первостепенно)

    def hover(self, locator):
        # return self.mouse.move_to_element(locator).perform()
        ActionChains(self.driver).move_to_element(self._is_visible(locator)).perform()

    def drag_and_drop(self, source, target):
        ActionChains(self.driver).drag_and_drop(self._is_visible(source), self._is_visible(target)).perform()

    def clicking_enter(self, locator):
        return self._is_clickable(locator).send_keys(Keys.RETURN)

    def scroll_to_element(self, locator):
        ActionChains(self.driver).move_to_element(self._is_visible(locator))

    def get_element_color(self, locator):
        return self._is_visible(locator).value_of_css_property('background-color')

# ДЗ: Написать шаблонный модуль и класс для страниц, фистуры, пробежаться по сайту и напиисать модули для того, что уже умею


# Логировать один метод(is visible):
# составить дубликат метода, дубликат под ним и пробовать. yield не использовать
