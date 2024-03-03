import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.check_and_validate import CheckAndValidatePage
from pages.input_and_click_page import InputAndClickPage
from pages.hover_and_select_page import HoverAndSelectPage
from pages.drag_and_drop_page import DragAndDropPage
from pages.chekboxes_and_scroll_page import CheckboxesAndScrollPage
from env_config import Config



@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


# @pytest.fixture(scope='function')
# def setup(get_webdriver):
#     url = 'https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html'
#     get_webdriver.get(url)
#     yield get_webdriver
#     get_webdriver.quit()


@pytest.fixture()
def index_page(get_webdriver):
    get_webdriver.get(Config.BASE_URL)
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture()
def check_and_validate_page(get_webdriver):
    get_webdriver.get(Config.CHECK_AND_VALIDATE_URL)
    yield CheckAndValidatePage(get_webdriver)
    get_webdriver.quit()

@pytest.fixture()
def input_and_click_page(get_webdriver):
    get_webdriver.get(Config.INPUT_AND_CLICK_URL)
    yield InputAndClickPage(get_webdriver)
    get_webdriver.quit()

@pytest.fixture()
def hover_and_select_page(get_webdriver):
    get_webdriver.get(Config.HOVER_AND_SELECT_URL)
    yield HoverAndSelectPage(get_webdriver)
    get_webdriver.quit()

@pytest.fixture()
def drag_and_drop_page(get_webdriver):
    get_webdriver.get(Config.DRAG_AND_DROP_URL)
    yield DragAndDropPage(get_webdriver)
    get_webdriver.quit()

@pytest.fixture()
def checkboxes_and_scroll_page(get_webdriver):
    get_webdriver.get(Config.CHECKBOXES_AND_SCROLL_URL)
    yield CheckboxesAndScrollPage(get_webdriver)
    get_webdriver.quit()



