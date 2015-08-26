import primes as ps

def legendre(a, p):
        if not ps.isPrime(p) or p == 2:
                print "Error: the Legendre symbol requires an odd prime."
                return
        if a % p == 0:
                return 0
        if a < -1:
                return legendre(-1, p) * legendre(-a, p)
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
        
        # Law of Quadratic Reciprocity
        if ps.isPrime(a):
                if a % 4 == 3 and p % 4 == 3:
                        return -1 * legendre(p, a)
                else:
                        return legendre(p, a)
        product = 1
        for prime in ps.primeFactors(a):
                product *= legendre(prime, p)
        return product

def jacobi(a, n):
        if n < 0 or n % 2 == 0:
                print "Error: the Jacobi symbol requires an odd positive integer."
                return
        if ps.isPrime(n):
                return legendre(a, n)
        
        pFactor = ps.primeFactorization(n)
        product = 1
        for term in pFactor:
                product *= legendre(a, term[0]) ** term[1]
        return product

def kronecker(a, n):
        if n < -1:
                return kronecker(a, -1) * kronecker(a, -n)
        if n == -1:
                if a < 0:
                        return -1
                return 1
        if n == 0:
                if a == 1 or a == -1:
                        return 1
                return 0
        if n == 2:
                if a % 2 == 0:
                        return 0
                elif a % 8 == 1 or a % 8 == 7:
                        return 1
                return -1
        if ps.isPrime(n) and n != 2:
                return legendre(a, n)
        
        pFactor = ps.primeFactorization(n)
        product = 1
        for term in pFactor:
                product *= kronecker(a, term[0]) ** term[1]
        return product
