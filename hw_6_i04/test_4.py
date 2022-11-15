import pytest
from issue04 import fit_transform


def test_names_various():
    """
    Тест проверяет, чтобы все наши элементы были разными
    """
    data = fit_transform(['Moscow', 'New York', 'Haifa', 'London'])
    result = [('Moscow', [0, 0, 0, 1]),
              ('New York', [0, 0, 1, 0]),
              ('Haifa', [0, 1, 0, 0]),
              ('London', [1, 0, 0, 0])]
    assert data == result


def test_names_equal():
    """
    Тест проверяет, чтобы в нашем списке были одинаковые элементы
    """
    data = fit_transform(['Moscow', 'Moscow', 'Moscow', 'New York'])
    result = [('Moscow', [0, 1]),
              ('Moscow', [0, 1]),
              ('Moscow', [0, 1]),
              ('New York', [1, 0])]
    assert data == result


def test_len():
    """
    Сравнивает длину списка с заданой константой
    """
    data = fit_transform(['Moscow', 'New York', 'Haifa'])
    test_len = 2
    assert len(data) != test_len


def test_if_empty():
    """
    Проверяет на исключение, в случае, когда ментод вызывается пустым
    """
    with pytest.raises(TypeError):
        fit_transform()