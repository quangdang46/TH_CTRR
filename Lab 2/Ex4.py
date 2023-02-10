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
# Ex4
table=list(itertools.product([False,True],repeat=3))

# p ∨ q → p ∧ q → ¬p ∨ ¬q
print("p\tq\tp V q\tp ∧ q\t¬p V ¬q\tp V q → p ∧ q → ¬p V ¬q")
for (p,q,r) in table:
	pOrq=lOr(p,q)
	pAndq=lAnd(p,q)
	notPOrnotQ=lOr(lNot(p),lNot(q))
	print(p,"\t",q,"\t",pOrq,"\t",pAndq,"\t",notPOrnotQ,"\t",lImplies(lImplies(pOrq,pAndq),notPOrnotQ))

# ¬p ∨ (q ∧ r) → r
print("p\tq\tr\t¬p\tq ∧ r\t¬p V (q ∧ r)\t¬p V (q ∧ r) → r")

for (p,q,r) in table:
	notP=lNot(p)
	qAndr=lAnd(q,r)
	notPOrqAndr=lOr(notP,qAndr)
	print(p,"\t",q,"\t",r,"\t",notP,"\t",qAndr,"\t",notPOrqAndr,"\t",lImplies(notPOrqAndr,r))

# (p → q) ∧ (q → r)
print("p\tq\tr\tp → q\tq → r\t(p → q) ∧ (q → r)")
for (p,q,r) in table:
	pq=lImplies(p,q)
	qr=lImplies(q,r)
	print(p,"\t",q,"\t",r,"\t",pq,"\t",qr,"\t",lAnd(pq,qr))