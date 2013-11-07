from math import e,pi

print(e)
print(pi)

print(e**2)
x = 0.0
while x < 2*pi:
    print (e**(x*1j))
    x += 0.01

# to rotate by tau degrees
# re**(theta*1j) * re**(tau*1j)
# = re**((theta+tau)*1j)
