from fractions import Fraction
import math
expo = Fraction('3/5')


def f(x):
    y = 5 * (pow((1.0 / x),(expo))  )
    g = (x / ((1 - x) * (1 - x)))
    z = pow(g  ,(expo))
    return 3.5 * (y + z)



xl=0
xu=1

ea=.5
i=0

print ("x     \t\t ea   \t\t xopt")
r = 0.61803398875
d= r*(xu - xl)
x1=xl+d
x2 = xu-d
f1=f(x1)

f2 = f(x2)

while ea > 0.1:
    if f1 > f2:
        xl = x2
        x2 = x1
        f2 = f1
        x1 = xl + r * (xu - xl)
        f1 = f(x1)
    else:
        xu = x1
        x1 = x2
        f1 = f2
        x2 = xu - r * (xu - xl)
        f2 = f(x2)
    if f1 > f2:
        xopt = x1
    else:
        xopt = x2

    if (i == 10):
        break

    ea = (0.38197 * (xu - xl) / xopt)
    print('%f \t %f \t %f ' % (i, ea, xopt*100))
    i += 1







