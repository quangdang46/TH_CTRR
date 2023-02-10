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