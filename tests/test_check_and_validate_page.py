from pytest import mark


case_1 = ['10', 'Valid']
case_2 = ['50', 'Valid']
case_3 = ['9', 'Not in range']
case_4 = ['51', 'Not in range']
case_5 = ['-', 'Not a number']
case_6 = ['-10', 'Negative integer']
case_7 = ['IO', 'Not a number']
case_8 = ['10.01', 'Not an integer']


@mark.parametrize('value, message', (case_1, case_2, case_3, case_4, case_5, case_6, case_7, case_8),
                  ids=['valid value min', 'valid value max', 'boundary value min-1', 'boundary value max+1', 'symbol',
                       'negative integer', 'letters', 'float'])
def test_check_value(check_and_validate_page, value, message):
    check_and_validate_page.enter_value(value=value)
    check_and_validate_page.check_message(msg=message)
