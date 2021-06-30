
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


def count_vowels(s):
    """counting number of vowels present"""
    vCount = 0
    str = s.lower()
    for i in str:
        if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
            vCount = vCount+1
    return (vCount)


def last_occurrence(target, sequence):
    """return the last occurrence of the index from the sequence"""
    location = "none"
    for offset, i in enumerate(sequence):
        if(target == i):
            location = offset
    return(location)


def my_enumerate(seq):
    """returns the sequence and their index respectively"""
    for i in seq:
       yield(seq.index(i), i)


