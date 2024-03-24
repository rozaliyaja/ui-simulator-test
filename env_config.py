from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    BASE_URL: str = "https://toghrulmirzayev.github.io/ui-simulator"
    CHECK_AND_VALIDATE_URL: str = f'{BASE_URL}/check_and_validate.html'
    INPUT_AND_CLICK_URL: str = f'{BASE_URL}/input-and-click.html'
    HOVER_AND_SELECT_URL: str = f'{BASE_URL}/hover_and_select.html'
    DRAG_AND_DROP_URL: str = f'{BASE_URL}/drag-and-drop.html'
    CHECKBOXES_AND_SCROLL_URL: str = f'{BASE_URL}/checkbox-and-scroll.html'
    SORTING_URL: str = f'{BASE_URL}/sorting.html'
    GAME_URL: str = f'{BASE_URL}/game.html'

class Creds:
    TEST_USERNAME = os.getenv('TEST_USERNAME')
    TEST_PASSWORD = os.getenv('TEST_PASSWORD')
