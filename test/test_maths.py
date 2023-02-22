import pytest
import sys
sys.path.append("/home/ubuntu/PycharmProjects/json-api/")
from maths import Maths


class TestMathsGetValue:
    @pytest.mark.parametrize("a, b", [("2", 5), (5, ""), (2, [1, 2, 3]), ({1}, 1)])
    def test_divide_type_error(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            Maths(a, b)
            raise TypeError("Неправильный тип данных")
        assert exc_info.type is TypeError

    @pytest.mark.parametrize("a, b", [(1, None), (None, 22), (None, None)])
    def test_divide_empty_value(self, a, b):
        with pytest.raises(TypeError) as exc_info:
            Maths(a, b)
            raise TypeError("Неправильный тип данных")
        assert exc_info.type is TypeError


class TestMethods:

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2),
        (2, 4, 0.5),
        (10, 0.5, 20)
    ])
    def test_divide(self, a, b, expected):
        m = Maths(a, b)
        assert m.divide == expected

    @pytest.mark.parametrize("a, b", [(2, 0), (0, 0)])
    def test_divide_zero_error(self, a, b):
        assert Maths(a, b).divide == "Нельзя делить на ноль"

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 8),
        (2, 4, 8),
        (10, 0.5, 5)
    ])
    def test_mull(self, a, b, expected):
        m = Maths(a, b)
        assert m.mull == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 6),
        (2, 4, 6),
        (10, 0.5, 10.5)
    ])
    def test_add(self, a, b, expected):
        m = Maths(a, b)
        assert m.add == expected

    @pytest.mark.parametrize("a, b, expected", [
        (4, 2, 2),
        (2, 4, -2),
        (10, 0.5, 9.5)
    ])
    def test_sub(self, a, b, expected):
        m = Maths(a, b)
        assert m.sub == expected
