import sys
import io
from functools import wraps


def redirect_output(filepath):
    """Декторатор, который перенаправляет вывод фукнции в файл"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            base_stdout = sys.stdout
            sys.stdout = io.StringIO()
            rt = func(*args, **kwargs)
            with open(filepath, 'w') as output:
                output.write(sys.stdout.getvalue())
            sys.stdout = base_stdout
            return rt
        return wrapper
    return decorator


@redirect_output('function_output.txt')
def calculate():
    """Расчет мощности для всех указанных чисел"""
    for power in range(1, 5):
        for num in range(1, 20):
            print(num ** power, end=' ')
        print()


if __name__ == '__main__':
    calculate()
    print('Результат выполнения функции лежит в function_output.txt')
