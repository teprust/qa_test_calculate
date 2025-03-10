from src.calc import calculate


def test_calc_division(): # тестирование деления
    assert calculate(10, 2, '/') == 5

def test_calc_subtraction(): # тестирование вычитания
    assert calculate(10, 2, '-') == 8
#
def test_calc_multiplication(): # тестирование умножение
    assert calculate(10, 2, '*') == 20
#
def test_calc_addition(): # тестирование cложения
    assert calculate(10, 2, '+') == 12
