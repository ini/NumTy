import primes

def legendre(a, p):
	if a % p == 0 or (not primes.isPrime(p)) or p == 2:
		return 0
	if a < -1:
		return legendre(-1, p) * legendre(a * -1, p)
	if a == -1:
		if p % 4 == 1:
			return 1
		else:
			return -1
	if a ** .5 == int(a ** .5):
		return 1
	if a == 2:
		if p % 8 == 1 or p % 8 == 7:
			return 1
		else:
			return -1
	if a > p:
		return legendre(a % p, p)
	elif primes.isPrime(a) and primes.isPrime(p):
		if a % 4 == 3 and p % 4 == 3:
			return -1 * legendre(p, a)
		else:
			return legendre(p, a)
	else:
		for prime in sieve(a):
			if a % prime == 0:
				return legendre(prime, p) * legendre(a / prime, p)
				break
