import unittest


class Fraction:
    """Fraction Class"""

    def __init__(self, n, d):
        """set numerator and denominator and Raise ValueError on 0 denominator"""
        self.n = n
        self.d = d
        if d == 0:
            raise ValueError('0 is an invalid denominator')
        elif(type(n) == str or type(d) == str):
            raise ValueError('Not an Integer')

    def __add__(self, other):
        """adding the two fractions"""
        a = self.n * other.d + self.d * other.n
        b = self.d * other.d
        return Fraction(a, b).simplify()

    def __sub__(self, other):
        """subtracting two fractions"""
        a = self.n * other.d - self.d * other.n
        b = self.d * other.d
        return Fraction(a, b).simplify()

    def __mul__(self, other):
        """multiplying the two fractions"""
        a = self.n * other.n
        b = self.d * other.d
        return Fraction(a, b).simplify()

    def __truediv__(self, other):
        """division of two fractions by simple approach"""
        a = self.n * other.d
        b = self.d * other.n
        return Fraction(a, b).simplify()

    def __eq__(self, other):
        """if the rwo fractions are equal returns True else False"""
        if (self.n*other.d) == (self.d*other.n):
            return True
        else:
            return False

    def __ne__(self, other):
        """if the two fractions are not equal returns True else False"""
        if self.n/self.d != other.n/other.d:
            return True
        else:
            return False

    def __lt__(self, other):
        """if the fraction is less then the other fraction return True else False"""
        if self.n/self.d < other.n/other.d:
            return True
        else:
            return False

    def __le__(self, other):
        """if the fraction is less then equal to the other fraction return True else False"""
        if self.n/self.d <= other.n/other.d:
            return True
        else:
            return False

    def __gt__(self, other):
        """if the fraction is greater then the other fraction return True else False"""
        if self.n/self.d > other.n/other.d:
            return True
        else:
            return False

    def __ge__(self, other):
        """if the fraction is greater then equal to the other fraction return True else False"""
        if self.n/self.d >= other.n/other.d:
            return True
        else:
            return False

    def simplify(self):
        i = 2
        while i <= self.d:
            if self.n % i == 0:
                if self.d % i == 0:
                    self.n = self.n / i
                    self.d = self.d / i
                    i = 1
            i = i + 1
        return self

    def __str__(self):
        """It returns fraction in String format"""
        return str(self.n) + "/" + str(self.d)


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

    def test_eq(self):
        """test fraction equality """
        f1 = Fraction(3, 4)
        f2 = Fraction(6, 8)
        f3 = Fraction(9, 12)
        self.assertTrue(f1 == f1)

    def test_add(self):
        """ test fraction addition """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        re1 = f1+f1
        re2 = Fraction(3,4)
        self.assertTrue((f1 + f1) == Fraction(3, 4))

    def test_sub(self):
        """ test fraction subtraction """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 - f1) == Fraction(0, 16))

    def test_mul(self):
        """ test fraction multiplication """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 * f1) == Fraction(9, 16))

    def test_truediv(self):
        """ test fraction division """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 / f1) == Fraction(12, 12))

    def test_ne(self):
        """ test fraction not equal """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 != f2))

    def test_lt(self):
        """ test fraction less then """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f3 < f2))

    def test_le(self):
        """ test fraction less then equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 <= f1))

    def test_gt(self):
        """ test fraction greater then """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 123)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 > f2))

    def test_ge(self):
        """ test fraction greater then equal to """
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)
        f3 = Fraction(1, 3)
        self.assertTrue((f1 >= f1))


if __name__ == '__main__':
    """there is no main(). Only test cases here"""
    unittest.main(exit=False, verbosity=2)
