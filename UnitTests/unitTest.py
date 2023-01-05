import unittest

def add(x, y):
  return x + y

class TestSum(unittest.TestCase):

  def test_add_integers(self):
    result = add(1, 2)
    self.assertEqual(result, 3)

  def test_add_floats(self):
    result = add(10.5, 2.5)
    self.assertEqual(result, 13.0)

if __name__ == '__main__':
  unittest.main()
