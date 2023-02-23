from math import *


# Ex2
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

# Ex3

def is_prime(n):
  if n==1:
    return False
  for i in range(2, n):
    if n%i==0:
      return False
  return True

def a():
	print("∃x ∈ Z,0 ≤ x ≤ 100, x3 < x")
	for x in range(101):
		if x**3<x:
			print("the given statement is correct when x equal to", x)
			return
	print("the given statement is incorrect for all values x within the given domain.")

def b():
	print("∃x ∈ Z, 0 ≤ x ≤ 100, and x is not even, x * 3 + 1 is not a prime number")
	for x in range(101):
		if x%2!=0 and not is_prime(x*3+1):
			print("the given statement is correct when x equal to", x)
			return
	print("the given statement is incorrect for all values x within the given domain.")

def c():
	print("∃x ∈ Z, 1 ≤ x, y ≤ 100, and x is not even, x * 5 + 3 is not a prime number")
	for x in range(1,101):
		if x%2!=0 and not is_prime(x*5+3):
			print("the given statement is correct when x equal to", x)
			return
	print("the given statement is incorrect for all values x within the given domain.")

def d():
	print("∃c ∈ Z,0 < c ≤ 100, c%4 != 0, ∀a, b ∈ Z +, c^2 = a^2 + b^2")
	for c in range(101):
		if c%4!=0 and c**2!=c**2+c**2:
			print("the given statement is correct when x equal to", c)
			return
	print("the given statement is incorrect for all values x within the given domain.")

def e():
	print("∃c ∈ Z,0 < c ≤ 100, c%5 != 0, ∀a, b ∈ Z +, c^2 = a^2 + b^2")
	for c in range(101):
		if c%4!=0 and c**2!=c**2+c**2:
			print("the given statement is correct when x equal to", c)
			return
	print("the given statement is incorrect for all values x within the given domain.")

def f():
	print("∀c ∈ Z, 0 < c ≤ 100, c^2> c")
	for c in range(101):
		if c**2<c:
			print("the given statement is incorrect when x equal to", x)
			return
		print("the given statement is correct for all values x within the given domain.")

a()
b()
c()
d()
e()
f()


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

# Ex5
import itertools
def lImplies(P,Q):
	if P:
		return Q
	return True

def lAnd(P,Q):
	if P:
		return Q
	return False

def lOr(P,Q):
	if not P:
		return Q
	return True

def lXor(P,Q):
	return P!=Q

def lNot(P):
	if P:
		return False
	return True

def lEquipvalent(P,Q):
	return P==Q

table=itertools.product([False,True],repeat=4)

def a():
	for (p,q,r,s) in table:
		if all([lImplies(p,r),lImplies(lNot(p),q),lImplies(q,s)]) and not lImplies(lNot(r),s):
			print("INVALID")
			break
	print("VALID")


def b():
	for (p,q,r,s) in table:
		if all([lImplies(p,q),lOr(lNot(r),s),lOr(p,r)]) and not lImplies(lNot(q),s):
			print("INVALID")
			break
	print("VALID")

def c():
	for (p,q,r,s,t) in table:
		if all([lImplies(p,lImplies(q,r)),lOr(p,s),lImplies(t,q),lNot(s)]) and not lImplies(lNot(r),lNot(t)):
			print("INVALID")
			break
	print("VALID")

def d():
	for (p,q,r,s) in table:
		if all([p,lImplies(p,r),lImplies(p,lOr(q,lNot(r))),lOr(lNot(q),lNot(s))]) and not s:
			print("INVALID")
			break
	print("VALID")

a()
b()
c()
d()