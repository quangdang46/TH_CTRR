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

table=itertools.product([False,True],repeat=4)

for (p,q,r,s) in table:
  if all([lImplies(p,r),lImplies(lNot(p),q),lImplies(q,s)]) and not lImplies(lNot(r),s):
    print("INVALID")
    break
else:
  print("VALID")

for (p,q,r,s) in table:
  if all([lImplies(p,q),lOr(lNot(r),s),lOr(p,r)]) and not lImplies(lNot(q),s):
    print("INVALID")
    break
else:
  print("VALID")


for (p,q,r,s,t) in table:
  if all([lImplies(p,lImplies(q,r)),lOr(p,s),lImplies(t,q),lNot(s)]) and not lImplies(lNot(r),lNot(t)):
    print("INVALID")
    break
else:
  print("VALID")


for (p,q,r,s) in table:
  if all([p,lImplies(p,r),lImplies(p,lOr(q,lNot(r))),lOr(lNot(q),lNot(s))]) and not s:
    print("INVALID")
    break
else:
  print("VALID")