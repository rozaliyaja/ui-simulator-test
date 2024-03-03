from pytest import mark
import allure

@allure.description('Successful input')
@allure.label('owner', 'Roza')  # нехорошая метрика
@allure.title('Successful input')
@allure.suite('input and click suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_input(input_and_click_page):
    input_and_click_page.enter_data(item='1')
    input_and_click_page.click_add_button()
    input_and_click_page.check_data_on_item_field(item='1')


@allure.description('Successful delete')
@allure.label('owner', 'Roza')  # нехорошая метрика
@allure.title('Successful delete')
@allure.suite('input and click suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_delete(input_and_click_page):
    input_and_click_page.enter_data(item='test')
    input_and_click_page.click_add_button()
    input_and_click_page.click_delete_button()
    input_and_click_page.check_item_fields_is_invisible()



