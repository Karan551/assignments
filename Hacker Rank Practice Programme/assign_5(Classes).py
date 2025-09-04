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
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real_part = self.real * no.real - self.imaginary * no.imaginary
        img_part = self.real * no.imaginary + no.real * self.imaginary

        return Complex(real_part, img_part)

    def __truediv__(self, no):
        try:
            denominator = no.real ** 2 + no.imaginary ** 2
            real_part = (self.real * no.real + self.imaginary * no.imaginary) / denominator
            img_part = (self.imaginary * no.real - self.real * no.imaginary) / denominator

            return Complex(real_part, img_part)

        except ZeroDivisionError as e:
            print("error", e)

    def mod(self):
        real_part = math.sqrt(self.real ** 2 + self.imaginary ** 2)
        return Complex(real_part, 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)

        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input("enter number separated by space:: ").split())
    d = map(float, input("enter number separated by space:: ").split())
    x = Complex(*c)
    y = Complex(*d)
    print("the value of x:", x)
    print("the value of y:", y)
    print(x + y)  # x.__add__(y)
    print(x - y)  # x.__sub__(y)
    print(x * y)  # x.__sub__(y)
    print("divide:: ", x / y)  # x.__sub__(y)
    print(x.mod())
    print(y.mod())

    # print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
