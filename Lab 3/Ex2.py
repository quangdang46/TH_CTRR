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