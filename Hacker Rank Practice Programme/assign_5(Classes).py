# c = map(float, input("Enter a number: ").split())
# print(list(c))
# print(list(c))
# print(complex(*c))


# lass
class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):

        print("Number is ", no)
        return f"N---{no},{type(no)}"

    def __sub__(self, no):
        pass

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % self.real
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % self.imaginary
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


c = map(float, input("Enter a number:- ").split())
d = map(float, input("Enter a number--- ").split())
x = Complex(*c)
y = Complex(*d)
# print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
print(str, x + y)
