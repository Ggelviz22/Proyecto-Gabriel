import unittest
from calculadora import suma, resta 

class PruebaCaculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(suma(5, 5), 10)
        self.assertEqual(suma(-9, 1), -8)

    def test_resta(self):
        self.assertEqual(resta(4, 4), 0)
        self.assertEqual(resta(15, 5), 10)

if __name__ == "__main__":
    unittest.main()
