def calculate(expression):

s = int(input('Введіть число: '))
b = int(input('Введіть число: '))
e = s-b
g = s+b
r = s*b
f = s/b
"""
 >>> 2+2 == 5
 False
 """
"""
 >>> 2+2 == 4
 True
 """
"""
 >>> s/0 
 False
 """

    return eval(expression)


