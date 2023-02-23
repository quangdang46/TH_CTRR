from math import *
# Ex4
def a():
  if sum( [(x+y)**2 for x in range(11) for y in range(11)] )> sum( [(x+2*y)**2 for x in range(10)  for y in range(10)] ):
    print("the given statement is correct")
  else:
    print("the given statement is incorrect")

def b():
  if factorial(20)< sum([factorial(x) for x in range(11)]):
    print("the given statement is correct")
  else:
    print("the given statement is incorrect")

def c():
  if sum([3*x**2 for x in range(11)]) >=10**3:
    print("the given statement is correct")
  else:
    print("the given statement is incorrect")

def d():
  if sum([4*x**3 + 6*x**2+2*x for x in range(5,11)])> 10**4+2*10**3+10**2-5**4-2*5**3-5**2:
    print("the given statement is correct")
  else:
    print("the given statement is incorrect")

a()
b()
c()
d()
