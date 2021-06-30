thisdict = {
    "+": "add",
    "-": "sub",
    "*": "mul",
    "/": "div",
    "=": "eq"
}


class Fraction:
    """Fraction Class"""

    def __init__(self, n, d):
        self.n = n
        self.d = d

    def add(self, other):
        a = self.n * other.d + self.d * other.n
        b = self.d * other.d
        return Fraction(a,b).simplify()

    def sub(self, other):
        a = self.n * other.d - self.d * other.n
        b = self.d * other.d
        f3 = Fraction(a, b)
        return f3

    def mul(self, other):
        a = self.n * other.n
        b = self.d * other.d
        f3 = Fraction(a, b)
        return f3

    def div(self, other):
        a = self.n * other.d
        b = self.d * other.n
        f3 = Fraction(a, b)
        return f3

    def eq(self, other):
        if self.n*other.d == self.d*other.n:
            return True
        else:
            return False

    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def simplify(self):
        i = 2
        while i <= self.d:
            if self.n % i == 0:
                if self.d % i == 0:
                    self.n = self.n / i
                    self.d = self.d / i
                    i = 1
            i = i + 1
        return str(self.n) + '/' + str(self.d)


def test():
    print("\n\n Test Cases")
    #     f12 = Fraction(1, 21)
    #     f44 = Fraction(4, 4)
    #     f128 = Fraction(12, 8)
    #     f32 = Fraction(3, 2)

    #     f5 = f12.add(f44).add(f128)
    #     print(f12, '+', f12, '=', f12.add(f12), '[4/4]')
    #     print(f44, '-', f12, '=', f44.sub(f12), '[4/8]')
    #     print(f12, '+', f44, '=', f12.add(f44), '[12/8]')
    #     print(f128, '==', f32, '=', f128.eq(f32), '[True]')
    #     print(f12, "+", f44, "+", f128, "=", f5, '[192/64]')


test()


print("Welcome to Factorial Calculator...")
n1 = int(input("Fraction 1 numerator:"))
d1 = int(input("Fraction 1 denominator:"))
n2 = int(input("Fraction 2 numerator:"))
d2 = int(input("Fraction 2 denominator:"))
try:
    if (d1 == 0 or d2 == 0):
        raise ValueError
except ValueError:
    print("Denominator cannot be Zero.")
    exit()
f1 = Fraction(n1, d1)
f2 = Fraction(n2, d2)
x = input("Operation (+, -, *, /, =):")
c = thisdict.get(x, "e")
if(c == "add"):
    print(f1.add(f2))
elif(c == "sub"):
    print(f1.sub(f2))
elif(c == "mul"):
    print(f1.mul(f2))
elif(c == "div"):
    print(f1.div(f2))
elif(c == "eq"):
    print(f1.eq(f2))
elif(c == "e"):
    print("Invalid Entry, Please enter a valid entry")
