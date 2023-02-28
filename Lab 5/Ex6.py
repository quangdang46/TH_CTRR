A=[
  [2 ,0 ,5 ,0 ,3 ,0],
  [3 ,0 ,0 ,0 ,0 ,0],
  [0 ,6 ,2 ,0 ,5 ,0],
  [3 ,0 ,9 ,0 ,25 ,0],
  [0 ,0 ,2 ,4 ,5 ,0],
  [0 ,0 ,0 ,0 ,0 ,5]
]
def isOdd(a):
  return a % 2 != 0
def isPrime(a):
  if a < 2:
    return False
  for i in range(2, a):
    if a % i == 0:
      return False
  return True

def isSquare(a):
  return a ** 0.5 == int(a ** 0.5)

def isGreater(a, b):
  return a > b

def isEqual(a, b):
  return a == b

def isAbove(a, b):
  row_a, col_a = a
  row_b, col_b = b
  return row_a < row_b

def isLeftOf(a, b):
  row_a, col_a = a
  row_b, col_b = b
  return col_a < col_b

def check_a(A):
  for row in A:
    for col in row:
      if not isOdd(col) and isPrime(col):
        return True
  return False

def check_b(A):
  for row in A:
    for col in row:
      if isOdd(col) and not isSquare(col):
        return False
  return True

def check_c(A):
  for row in A:
    for col in row:
      if isOdd(col) and not isGreater(col, 2):
        return False
  return True

def check_d(A):
  for row in A:
    for col in row:
      if isPrime(col) and (isGreater(col, 3) or isEqual(col, 3)):
        return True
  return False

def check_e(A):
  check=False
  for row in A:
    for col in row:
      if isOdd(col):
        check=True
        break
    if check:
      break
  if not check:
    return False
  for row in A:
    for col in row:
      if not isLeftOf((A.index(row), row.index(col)), (A.index(row), row.index(col))):
        return False
  return True

def check_f(A):
  check=False
  for row in A:
    for col in row:
      if isGreater(row,col) and isAbove(row,col):
        check=True
        break
    if check:
      break
  return check

