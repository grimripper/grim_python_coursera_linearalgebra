class Vec:
    def __init__(self, labels, function):
        self.D = labels
        self.f = function

def zero_vec(D):
    return Vec(D, {})

def setitem(v, d, val):
    v.f[d] = val

def getitem(v, d):
    if d in v.f:
        return v.f[d]
    else:
        return 0

v = Vec({'a','b','c'}, {'a':1})
print('v.D = ', v.D)
print('v.f = ', v.f)

for d in v.D:
    if d in v.f:
        print(v.f[d])

v = zero_vec({0,1,2,3,4})
setitem(v, 0, 'a')
print(v.f[0])

print(getitem(v,0))
print(getitem(v,1))