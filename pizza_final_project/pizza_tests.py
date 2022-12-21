from pizza import *
import pytest


@pytest.mark.parametrize('s,exp', [(Margherita(), 'tomato_sause, mozzarella, tomatoes'),
                                   (Pepperoni(), 'tomato_sause, mozzarella, pepperoni'),
                                   (Hawaiian(), 'tomato_sause, mozzarella, chiken, pineapples'),
                                   (BabyCarrot(), 'tomato_sause, mozzarella, babycarrot')])
def test_recipes(s, exp):
    """Тестируем рецепты"""
    assert s.dict() == exp


random.seed(10)


def test_bake():
    """Тестируем декоратор и функцию bake"""
    assert bake() == 'bake - 19 минут!'


@pytest.mark.parametrize('s,exp', [(Hawaiian('S'), 'L'),
                                   (Pepperoni('XL'), 'XL'),
                                   (BabyCarrot('L'), 'L')])
def test_size(s, exp):
    """Тестируем размеры"""
    assert s.size == exp
