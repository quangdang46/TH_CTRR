def is_prime(n):
	if n == 1:
		return False
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(3, int(n**0.5)+1, 2):
		if n % i == 0:
			return False
	return True

def next_prime(n):
	n += 1
	while not is_prime(n):
		n += 1
	return n

print(next_prime(8))