import unittest
from issue03 import fit_transform


class TestFitTransform(unittest.TestCase):
    def test_names_various(self):
        """
        Тест проверяет, чтобы все наши элементы были разными
        """
        data = fit_transform(['Moscow', 'New York', 'Haifa', 'London'])
        result = [('Moscow', [0, 0, 0, 1]),
                  ('New York', [0, 0, 1, 0]),
                  ('Haifa', [0, 1, 0, 0]),
                  ('London', [1, 0, 0, 0])]
        self.assertEqual(data, result)

    def test_names_equal(self):
        """
        Тест проверяет, чтобы в нашем списке были одинаковые элементы
        """
        data = fit_transform(['Moscow', 'Moscow', 'Moscow', 'New York'])
        result = [('Moscow', [0, 1]),
                  ('Moscow', [0, 1]),
                  ('Moscow', [0, 1]),
                  ('New York', [1, 0])]
        self.assertEqual(data, result)

    def test_len(self):
        """
        Сравнивает длину списка с заданой константой
        """
        data = fit_transform(['Moscow', 'New York', 'Haifa'])
        test_len = 2
        self.assertFalse(len(data) == test_len)

    def test_if_empty(self):
        """
        Проверяет на исключение, в случае, когда ментод вызывается пустым
        """
        with self.assertRaises(TypeError):
            fit_transform()


if __name__ == '__main__':
    unittest.main()
