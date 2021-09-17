import unittest

def f():
    return 5

class MyTestCase(unittest.TestCase):
    def test_something(self):

        self.assertEqual(f(), 2+2)

if __name__ == '__main__':
    unittest.main()

# python -m unittest test
