import pytest
from issue02 import decode


@pytest.mark.parametrize("test, expected",
                         [('-- .- .. -....- .--. -.-- - .... --- -. -....- ..--- ----- .---- ----.', 'MAI-PYTHON-2019'),
                          (' ', ''),
                          ('..--- ...-- ----- ..--- ..--- ----- ----- -----', '23022000'),
                          ('.- ...- .. - --- -....- .- -.-. .- -.. . -- -.--', 'AVITO-ACADEMY')])
def test_decode(test, expected):
    """
    Проверяет наши тесты
    """
    assert decode(test) == expected


def main():
    pass


if __name__ == '__main__':
    main()
