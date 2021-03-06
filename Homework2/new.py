class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, a):
        self.num = self.num * a.den + self.den * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def __sub__(self, a):
        self.num = self.num * a.den - self.den * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def __mul__(self, a):
        self.num = self.num * a.num
        self.den = self.den * a.den
        return self.simplify(self.num, self.den)

    def __div__(self, a):
        self.num = self.num * a.den
        self.den = self.den * a.num
        return self.simplify(self.num, self.den)

    def __pow__(self, power):
        self.num = self.num**power
        self.den = self.den**power
        return self.simplify(self.num, self.den)

    def simplify(self, num, den):
        self.num = num
        self.den = den
        i = 2
        while i <= self.den:
            if self.num % i == 0:
                if self.den % i == 0:
                    self.num =self.num/ i
                    self.den =self.den/ i
                    i = 1
            i = i+ 1
        return str(self.num) + '/' + str(self.den)

    # def decimal(self, accuracy=3):
    #     return round(float(self.num)/float(self.den), accuracy)

f1 = Fraction(3, 4)
f2 = Fraction(1, 2)
f3 = Fraction(1, 3)
print(f1 + f1)
print(Fraction(24, 16))