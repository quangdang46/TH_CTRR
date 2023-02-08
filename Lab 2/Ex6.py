def a(p, q, r, s):
    if (not p or r) and (not p or q) and (q or s):
        return True
    else:
        return False
    
def b(p, q, r, s, t):
    if (p or not q or r) and (p or s) and (t or q) and (not s):
        return True
    else:
        return False
    
def c(p, q, r, s):
    if (p or not q) and (not r or s) and (p or r):
        return True
    else:
        return False

def d(p, q, r, s):
    if p and (p or r) and (p or q or not r) and (not q or not s):
        return True
    else:
        return False


p=True
q=True
r=True
s=True
t=True

print(a(p, q, r, s))
print(b(p, q, r, s, t))
print(c(p, q, r, s))
print(d(p, q, r, s))
