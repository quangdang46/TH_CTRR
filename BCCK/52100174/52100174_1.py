def euclidean_algorithm(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = euclidean_algorithm(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def find_modular_inverse(a, n):
	gcd, x, y = euclidean_algorithm(a, n)
	if gcd != 1:
		return None
	return x % n

a = 4
n = 8
mod_inv = find_modular_inverse(a, n)
print(mod_inv) # output: None

