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