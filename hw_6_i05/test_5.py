from unittest.mock import patch, MagicMock
import urllib.request
import pytest
import io
from issue05 import what_is_year_now


def test_date_dash():
    """
    Тест проверяет дату через тире
    """
    date = io.StringIO('{"currentDateTime": "2022-11-14T00:00Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        result = what_is_year_now()
    true_result = 2022
    assert result == true_result


def test_date_dots():
    """
    Тест проверяет дату через точки
    """
    date = io.StringIO('{"currentDateTime": "14.11.2022T00:00Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        result = what_is_year_now()
    true_result = 2022
    assert result == true_result


def test_date_format():
    """
    Тест сравнивает формат полученной даты и тестовой даты
    """
    date = io.StringIO('{"currentDateTime": "01/12/2020T21:29Z"}')
    with patch.object(urllib.request, 'urlopen', return_value=date):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_no_date():
    """
    Тест проверяет есть ли дата
    """
    no_date = io.StringIO('{"ML": "Boosting"}')
    urllib.request.urlopen = MagicMock(return_value=no_date)
    with pytest.raises(KeyError):
        what_is_year_now()


def main():
    pass


if __name__ == '__main__':
    main()