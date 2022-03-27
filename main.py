import math
import cmath

print("Введите коэффициенты для уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
 
d = b ** 2 - 4 * a * c
print("Дискриминант D = %.2f" % d)
 
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
elif d == 0:
    x = -b / (2 * a)
    print("x = %.2f" % x)
elif d < 0:
    x1 = (-b-cmath.sqrt(d))/(2*a)
    x2 = (-b+cmath.sqrt(d))/(2*a)
    print("x1 = " + "{0.real:.3f}{0.imag:+.3f}j".format(x1) + "\nx2 = " + "{0.real:.3f}{0.imag:+.3f}j".format(x2))