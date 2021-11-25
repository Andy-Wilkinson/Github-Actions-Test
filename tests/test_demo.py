import pytest
from ghactionstest.demo import add, subtract


class TestDemo(object):
    @pytest.mark.parametrize("a,b,result", [
        (1, 2, 3),
        (2, 2, 4),
        (3, 2, 5)
    ])
    def test_add(self, a: int, b: int, result: int):
        assert add(a, b) == result

    @pytest.mark.parametrize("a,b,result", [
        (1, 2, -1),
        (2, 2, 0),
        (3, 2, 1)
    ])
    def test_subtract(self, a: int, b: int, result: int):
        assert subtract(a, b) == result
