from support.assertion_errors import AssertionErrors


class Assertions:
    @staticmethod
    def assert_equal(actual: object,
                     expected: object) -> object:  # object-это для меня или для др спеца, который будет читать код
        assert actual == expected, AssertionErrors.ASSERT_EQUAL.format(expected, actual)

    # написать assert boolean(использовать is)

    @staticmethod
    def assert_boolean(actual):
        assert actual is True, AssertionErrors.ASSERT_BOOLEAN
        # try:
        #
        # except AssertionError:
        #     raise AssertionError(AssertionErrors.ASSERT_BOOLEAN)
# assert actual is True, AssertionErrors.ASSERT_BOOLEAN
