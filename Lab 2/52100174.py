import itertools
# Ex1
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

# Ex2
P=[True,True,False,False]
Q=[True,False,True,False]

def lLImplies(P,Q):
	return [lImplies(p,q) for p,q in zip(P,Q)]

def lLAnd(P,Q):
	return [lAnd(p,q) for p,q in zip(P,Q)]

def lLOr(P,Q):
	return [lOr(p,q) for p,q in zip(P,Q)]

def lLXor(P,Q):
	return [lXor(p,q) for p,q in zip(P,Q)]

def lLNot(P):
	return [lNot(p) for p in P]

def lLEquipvalent(P,Q):
	return [lEquipvalent(p,q) for p,q in zip(P,Q)]

print(lLImplies(P,Q))
print(lLAnd(P,Q))
print(lLOr(P,Q))
print(lLXor(P,Q))
print(lLNot(P))
print(lLEquipvalent(P,Q))

# Ex3
table=list(itertools.product([False,True],repeat=3))
print("p\tq\tr\tp∧q->r")
for (p,q,r) in table:
	print(p,"\t",q,"\t",r,"\t",lImplies(lAnd(p,q),r))

print("p\tq\tr\tr->p∧q")
for (p,q,r) in table:
	print(p,"\t",q,"\t",r,"\t",lImplies(r,lAnd(p,q)))

# Ex4
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



# Ex6


tablepqrs=list(itertools.product([False,True],repeat=4))
tablepqrst=list(itertools.product([False,True],repeat=5))
def a(table):
	for (p,q,r,s) in table:
		if all([lImplies(p,q),lImplies(lNot(p),q),lImplies(q,s)]) and not lImplies(lNot(r),s):
			return "INVALID"
	return "VALID"

def c(table):
	for (p,q,r,s) in table:
		if all([lImplies(p,q),lOr(lNot(r),s),lOr(p,r)]) and not lImplies(lNot(q),s):
			return "INVALID"
	return "VALID"

def b(table):
	for (p,q,r,s,t) in table:
		if all([lImplies(p,lImplies(q,r)),lOr(p,s),lImplies(t,q),lNot(s)]) and not lImplies(lNot(r),lNot(t)):
			return "INVALID"
	return "VALID"

def d(table):
	for (p,q,r,s) in table:
		if all([p,lImplies(p,r),lImplies(p,lOr(q,lNot(r))),lOr(lNot(q),lNot(s))]) and not s:
			return "INVALID"
	return "VALID"


print(a(tablepqrs))
print(b(tablepqrst))
print(c(tablepqrs))
print(d(tablepqrs))