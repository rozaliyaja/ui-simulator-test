from pytest import mark
import allure


@allure.description('Success login')
@allure.label('owner', 'Roza')  # нехорошая метрика
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    index_page.enter_username(user_name='correct_username')
    index_page.enter_password(password='correct_password')
    index_page.clicking_by_enter_instead_of_click()
    index_page.check_url()


case_1 = ['', '', 'Username and password fields cannot be empty']
case_2 = ['correct_username', 'incorrect_password', 'Password or username is incorrect']
case_3 = ['incorrect_username', 'correct_password', 'Password or username is incorrect']


@mark.parametrize('user_name, password, error_msg', (case_1, case_2, case_3),
                  ids=['without username and password', 'with_incorrect_password', 'with_incorrect_username'])
def test_unsuccessful_login(index_page, user_name, password, error_msg):
    index_page.enter_username(user_name=user_name)
    index_page.enter_password(password=password)
    index_page.clicking_by_enter_instead_of_click()
    index_page.check_error_message(error_msg=error_msg)

#
def test_check_login_btn_color(index_page):
    index_page.check_login_btn_element_color('rgba(139, 195, 74, 1)')# Спросить у Тогги про цвет, как будтоо всегда меняетсяя



