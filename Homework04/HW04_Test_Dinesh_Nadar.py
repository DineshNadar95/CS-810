import unittest
from HW04_Dinesh_Nadar import Fraction, count_vowels, last_occurrence, my_enumerate


class TestFraction(unittest.TestCase):
    def test_init(self):
        """ verify that the numerator and denominator are set properly """
        f = Fraction(3, 4)
        self.assertEqual(f.n, 3)
        self.assertEqual(f.d, 4)

    def test_str(self):
        """ verify that __str__() works properly """
        f = Fraction(3, 4)
        self.assertEqual(str(f), '3/4')
        self.assertEqual(str(f), '2/4')

    def test_eq(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 13)
        self.assertTrue(f1 == f1)
        self.assertTrue(f1 == f3)

    def test_add(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 + f1) == Fraction(3, 4))
        self.assertTrue((f1 + f2) == Fraction(3, 4))

    def test_sub(self):
        """ test fraction subtraction """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 - f1) == Fraction(0, 16))
        self.assertTrue((f1 - f3) == Fraction(1, 6))

    def test_mul(self):
        """ test fraction multiplication """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 * f1) == Fraction(9, 16))
        self.assertTrue((f1 * f2) == Fraction(3, 10))

    def test_truediv(self):
        """ test fraction division """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 / f1) == Fraction(12, 12))
        self.assertTrue((f1 / f2) == Fraction(1, 6))

    def test_ne(self):
        """ test fraction not equal """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 != f2))
        self.assertTrue((f1 != f1))

    def test_lt(self):
        """ test fraction less then """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f3 < f2))
        self.assertTrue((f1 < f2))

    def test_le(self):
        """ test fraction less then equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 <= f1))
        self.assertTrue((f1 <= f3))

    def test_gt(self):
        """ test fraction greater then """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 123)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 > f2))
        self.assertTrue((f3 > f1))

    def test_ge(self):
        """ test fraction greater then equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 >= f1))
        self.assertTrue((f2 >= f1))

    def test_simplify(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue((f2) == Fraction(3, 4))
        self.assertTrue((f3) == Fraction(3, 8))


class TestIteration(unittest.TestCase):

    def test_count_vowels(self):
        """test count of vowels"""
        self.assertEqual(count_vowels('hello world'), 3)
        self.assertEqual(count_vowels('hEllO wrld'), 2)
        self.assertEqual(count_vowels('hll wrld'), 1)

    def test_last_occurrence(self):
        """test the last occurrence"""
        self.assertEqual(last_occurrence("e", 'hello'), 1)
        self.assertEqual(last_occurrence("o", 'hello world'), 7)
        self.assertEqual(last_occurrence("d", 'hello world'), 3)

    def test_my_enumerate(self):
        """test enumerate function"""
        self.assertTrue(list(my_enumerate("HI!")) == list(enumerate("HI!")))
        self.assertTrue(list(my_enumerate("HI!")) == list(enumerate("HIE!")))


if __name__ == '__main__':
    """there is no main(). Only test cases here"""
    unittest.main(exit=False, verbosity=2)
