class TP:
    def __init__(self, x):
        self.x = x

    def __radd__(self, other):
        print('invoked')
        return ComplexNumber(self.x,0)

class ComplexNumber:
    def __init__(self, r, i):
        self.real = r
        self.imag = i

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        else:
            return NotImplemented

    def __repr__(self):
        return "ComplexNumber(" + str(self.real) + "," + str(self.imag) + ")"


complexNum2 = ComplexNumber(1, 2)
print(complexNum2)

complexNum3 = ComplexNumber(1,1)

complexNum4 = complexNum2 + complexNum3

complexNum4 = complexNum2 + TP(3)

print(complexNum4)

