
def is_prime(n):
  if n==1:
    return False
  for i in range(2, n):
    if n%i==0:
      return False
  return True
def a():
  result=False
  for x in range(0, 101):
    if x**3 < x:
      result=True
      print("the given statement is correct when x equal to", x)
      return
  if result==False:
    print("the given statement is incorrect for all values x within the given domain.")
def b():
  result=False
  for x in range(0, 101):
    if x%2==0 and is_prime(x*3+1):
      result=True
      print("the given statement is correct when x equal to", x)
      return
  if result==False:
    print("the given statement is incorrect for all values x within the given domain.")
  
def c():
  result=False
  for x in range(1, 101):
    for y in range(1, 101):
      if x%2==0 and is_prime(x*5+3):
        result=True
        print("the given statement is correct when x equal to", x, "and y equal to", y)
        return
  if result==False:
    print("the given statement is incorrect for all values x within the given domain.")

# d e f
