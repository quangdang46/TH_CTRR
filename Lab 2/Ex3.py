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

# Ex3
table=list(itertools.product([False,True],repeat=3))
print("p\tq\tr\tp∧q->r")
for (p,q,r) in table:
	print(p,"\t",q,"\t",r,"\t",lImplies(lAnd(p,q),r))

print("p\tq\tr\tr->p∧q")
for (p,q,r) in table:
	print(p,"\t",q,"\t",r,"\t",lImplies(r,lAnd(p,q)))