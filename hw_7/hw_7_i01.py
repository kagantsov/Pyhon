import sys
from datetime import datetime

original_write = sys.stdout.write


def my_write(string_text):
    """Добавляем к тексту string_text информацию о текущем времени"""
    current_datetime = str(datetime.now().replace(microsecond=0))
    if string_text != '\n':
        original_write(f'[{current_datetime}]: {string_text} \n')


if __name__ == '__main__':
    sys.stdout.write = original_write

    print('1, 2, 3')

    sys.stdout.write = my_write

    print('1, 2, 3')
