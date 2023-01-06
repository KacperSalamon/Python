import unittest

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(2, -3), -1)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-2, 3), -5)
        self.assertEqual(subtract(2, -3), 5)

if __name__ == '__main__':
    unittest.main()
