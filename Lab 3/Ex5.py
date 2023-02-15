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