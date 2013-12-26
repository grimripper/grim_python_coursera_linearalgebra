class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function


v = Vec({'a','b','c'}, {'a':1})
print('v.D = ', v.D)
print('v.f = ', v.f)

for d in v.D:
    if d in v.f:
        print(v.f[d])
