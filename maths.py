import logging

maths_logger = logging.getLogger("maths_logger")


class Maths:
    def __init__(self, a=None, b=None):
        self._a = a
        self._b = b

    @property
    def var_a(self):
        return self.__check_type_data(self._a)

    @property
    def var_b(self):
        return self.__check_type_data(self._b)

    def __check_type_data(self, value):
        if not isinstance(value, (int, float)):
            maths_logger.error(TypeError)
            raise TypeError("Неправильный тип данных")

        else:
            return value

    #
    @property
    def divide(self):
        try:
            return self.var_a / self.var_b
        except ZeroDivisionError:
            maths_logger.error(ZeroDivisionError, exc_info=True)
            return "Нельзя делить на ноль"

    @property
    def mull(self):
        return self.var_a * self.var_b

    @property
    def add(self):
        return self.var_a + self.var_b

    @property
    def sub(self):
        return self.var_a - self.var_b
