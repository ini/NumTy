import congruences as congr
import quadratic_residues as qr
import primes as ps

n = 7  # For Legendre, Jacobi and Kronecker symbol evaluation

def gcd(a, b):
  return congr.gcd(a, b)

def legendre(a):
  return qr.legendre(a, n)

def jacobi(a):
  return qr.jacobi(a, n)

def kronecker(a):
  return qr.kronecker(a)

def one(n):
	return 1

def Id(n):
	return n
	
def e(n):
	if n == 1:
		return 1
	return 0
	
def eulerPhi(n):
	if n == 1:
		return 1
	product = n
	primes = ps.sieve(n)
	for p in primes:
		if n % p == 0:
			product *= (1 - 1.0 / p)
	return product
	
def mobius(n):
	count = 0
	pFactor = ps.primeFactorization(n)
	for term in pFactor:
		if term[1] != 1:
			return 0
		count += 1
	if count % 2 == 0:
		return 1
	return -1
	
def d(n):
	if n == 0:
		return 0
	product = 1
	pFactor = ps.primeFactorization(n)
	for term in pFactor:
		product *= term[1] + 1
	return product
	
def sigma(n):
	if n == 0:
		return 0
	product = 1
	pFactor = ps.primeFactorization(n)
	for term in pFactor:
		product *= (term[0] ** (term[1] + 1) - 1) / (term[0] - 1)
	return product
	
def convolution(f, g, n):
	sum = eval(f + "(" + str(n) + ")")
	for d in xrange(1, n/2 + 1):
		if n % d == 0:
			sum += eval(f + "(" + str(d) + ")") * eval(g + "(" + str(n/d) + ")")
	return sum
