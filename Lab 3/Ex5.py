def nega(A):
  if A[0:3] == "For":
      print("Exist",A[4:])
  elif A[0:4] == "Exist":
      print("For all",A[5:])
  else:
      print("Error")
nega("For all fishes, they need water to survive.")
nega("Exist a person, who is left handed")
nega("Exist an employee in the company, who is late to work everyday.")
nega("For all fishes in this pond, they are Koi fish.")
nega("There is at least one creature in the ocean, it can live on land")
nega("Every students in class A did not pass the test")
