# # Ex1
print("D is 'fishes'")
print("P is 'need water to survive'")
print("Formal form: For all x in D, P(x)")

print("D is 'person'")
print("P is 'is left handed'")
print("Formal form: Exist x in D such that P(x)")

print("D is 'employee in the company'")
print("P is 'is late to work everyday'")
print("Formal form: Exist x in D such that P(x)")


print("D is 'fishes in this pond'")
print("P is 'are Koi fish'")
print("Formal form: For all x in D, P(x)")

print("D is 'creature in the ocean'")
print("P is 'can live on land'")
print("Formal form: Exist x in D such that P(x)")

print("D is 'students in class A'")
print("P is 'did not pass the test'")
print("Formal form: For all x in D, P(x)")

# Ex2
listExpression=['For all fishes, they need water to survive',
                "Exist a person, who is left handed",
                "Exist an employee in the company, who is late to work everyday",
                "For all fishes in this pond, they are Koi fish",
                "There is at least one creature in the ocean, it can live on land",
]
def formalConvert(S):
	list_=["For all","Exist","There is at least one"]
	arr=S.split(",")
	D=arr[0].replace(list(filter(lambda x:x in arr[0],list_))[0],"").strip()
	P=" ".join(arr[1].strip().split()[1:])
	return [D,P]
for s in listExpression:
	print(formalConvert(s))
# Ex3
D = "people"
P = "is blond"
Q = "is westerner"
print("For all", D, ", if they are", P, "then they are", Q)


D = "person"
P = "hair is black"
Q = "is westerner"
print("Exist a", D, ", whose", P, "but is a", Q)

D = "students"
P = "study correctly"
Q = "have high score"
print("For all", D, ", if they", P, "then they", Q)

D = "mammal"
P = "live in the sea"
Q = "dolphins or whales"
print("For every", D, ", if they", P, ", they are either", Q)

D = "birds"
P = "don't have wings and can swim"
Q = "are penguins"
print("For every", D, ", if they", P, ", then they",Q)

D = "birds"
P = "have wings but can't fly"
print("Exist a ",D,"that ",P )

# Ex4
listExpression=[
	"For all people, if they are blond then they are westerners",
	"Exist a person, whose hair is black but is a westerner",
	"For all students, if they study correctly then they have high score",
	"For every mammal, if they live in the sea, they are either dolphins or whales",
	"For every bird, if they don't have wings and can swim then they are penguins",
	"Exist a bird, who have wing but can't fly"
]
def formalConvertPQ(S):
	mappings = {
		"people": ("people", "is blond", "is westerner"),
		"students": ("students", "study correctly", "have high score"),
		"mammal": ("mammal", "live in the sea", "are either dolphins or whales"),
		"bird": ("birds", "don't have wings and can swim", "are penguins"),
		"a bird": ("birds", "have wings but can't fly", ""),
		"a person":("a person","hair is black","is westerner")
	}
	list_=["For all","Exist","For every"]
	arr=S.split(",")
	D=arr[0].replace(list(filter(lambda x:x in arr[0],list_))[0],"").strip()
	if D not in mappings:
		return "", "", "", "Error: Invalid input string"
	D, P, Q = mappings[D]
	if Q:
		F = f"For all {D}, if they {P}, then they {Q}."
	else:
		F = f"Exist a {D} that {P}."

	return [D, P, Q, F]


for s in listExpression:
	print(formalConvertPQ(s))

# Ex5
listExpression=["For all fishes, they need water to survive",
				"Exist a person, who is left handed",
				"Exist an employee in the company, who is late to work everyday",
				"For all fishes in this pond, they are Koi fish",
				"There is at least one creature in the ocean, it can live on land"]
def nega(S):
	list_=["For all","Exist","There is at least one"]

	neagation={
		"For all":lambda x,y:"There exist "+x+ "such that not "+y,
		"Exist":lambda x,y:"For every "+x+", not "+y,
		"There is at least one":lambda x,y:"not "+x+", "+y
	}
	arr=S.split(",")
	negaWord=list(filter(lambda x:x in arr[0],list_))[0]
	D=arr[0].replace(negaWord,"").strip()
	P=" ".join(arr[1].strip().split()[1:])
	try:
		return neagation[negaWord](D,P)
	except KeyError:
		print("Invalid negaWord")
	return None

print("----------------------------\n")
for s in listExpression:
	print(nega(s))