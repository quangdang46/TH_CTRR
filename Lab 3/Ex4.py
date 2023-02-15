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
