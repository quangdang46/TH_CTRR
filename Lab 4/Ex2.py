from math import sqrt

def a():
  for x in range(0, 101):
    if x**2 == 15**2 + 16**2:
      print("the given statement is correct when x equal to", x)
      return
  print("the given statement is incorrect for all values x within the given domain.")

def b():
  for x in range(0, 101):
    if x**2 == 12**2 + 16**2:
      print("the given statement is correct when x equal to", x)
      return
  print("the given statement is incorrect for all values x within the given domain.")

def c():
  for x in range(-50, 51):
    if x**2 >= 99*x:
      print("the given statement is correct when x equal to", x)
      return
  print("the given statement is incorrect for all values x within the given domain.")

def d():
  for x in range(50, 101):
    if (x*(x+1)*(x+2))%6 != 0:
      print("the given statement is correct when x equal to", x)
      return
  print("the given statement is incorrect for all values x within the given domain.")

def e():
  for x in range(0, 101):
    for y in range(0, 101):
      if sqrt(x+y) == sqrt(x) + sqrt(y):
        print("the given statement is correct when x equal to", x, "and y equal to", y)
        return
  print("the given statement is incorrect for all values x within the given domain.")

a()
b()
c()
d()
e()