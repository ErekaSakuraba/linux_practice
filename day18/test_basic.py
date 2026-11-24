import unittest

def add_numbers(a, b):
    return a + b

def divide_numbers(a, b):
    return a / b


class TestAddNumbers(unittest.TestCase):

    def test_add_numbers(self):
        result = add_numbers(3, 5)

        # ここにテストを書く！
        self.assertEqual(result, 8)

    def test_add_numbers_zero(self):
        result = add_numbers(0, 5)
        self.assertEqual(result, 5)

    def test_add_numbers_negative(self):
        result = add_numbers(-3, 5)
        self.assertEqual(result, 2)


class TestDivideNumbers(unittest.TestCase):

    def test_divide_numbers(self):
        result = divide_numbers(10, 2)
        self.assertEqual(result, 5)

    def test_divide_numbers_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide_numbers(10, 0)


if __name__ == "__main__":
    unittest.main()