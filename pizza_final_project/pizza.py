import random


class MainPizza:
    """Класс со всеми ингридиентами"""

    def __init__(self, size='L'):
        """Определяем возможные ингредиенты пиццы и размер"""
        self.tomato_sause = True
        self.mozzarella = True
        self.tomatoes = False
        self.pepperoni = False
        self.chiken = False
        self.pineapples = False
        self.babycarrot = False
        if size == 'XL':
            self.size = 'XL'
        else:
            self.size = 'L'

    def dict(self):
        """Возвращаем список ингредиентов"""
        return ', '.join(list({key: value for key, value in self.__dict__.items()
                               if value and key != 'size'}.keys()))


class Margherita(MainPizza):
    """Класс для пиццы маргарита"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.tomatoes = True


class Pepperoni(MainPizza):
    """Класс для пиццы пепперони"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.pepperoni = True


class Hawaiian(MainPizza):
    """Класс для гавайской пиццы"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.chiken = True
        self.pineapples = True


class BabyCarrot(MainPizza):
    """Класс для пиццы с мини-морковью"""
    def __init__(self, size='L'):
        super().__init__(size)
        self.babycarrot = True


def log(function):
    """Декоратор который выводит имя функции и время выполнения"""
    def func():
        return f'{function.__name__} - {random.randint(10, 20)} минут!'
    return func


@log
def bake():
    """Готовит пиццу"""
    pass


if __name__ == '__main__':
    pass
