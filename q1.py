__author__ = 'Eutimio'
import math
def distancia(x1, y1, x2, y2):
    a=x1+y1
    b=y2+x2
    c=a*a + b*b
    c1=math.sqrt(c)
    return c1
x1= int(input("enter size for x1"))
y1= int(input("enter size for y1"))
x2= int(input("enter size for x2"))
y2= int(input("enter size for y2"))
d= distancia(x1, y1, x2, y2)
print(d)
