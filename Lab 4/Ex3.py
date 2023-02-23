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