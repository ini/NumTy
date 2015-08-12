import math
import random
import congruences as congr


def miller_rabin_pass(a, n):
        d = n - 1
        s = 0
        while d % 2 == 0:
                d >>= 1
                s += 1
        a_to_power = pow(a, d, n)
        if a_to_power == 1:
                return True
        for i in xrange(s-1):
                if a_to_power == n - 1:
                        return True
                a_to_power = (a_to_power * a_to_power) % n
        return a_to_power == n - 1

def isPrime(n):
        if n < 2:
                return False
        # Uses Miller-Rabin primality test
        for repeat in xrange(20):
                a = 0
                while a == 0:
                        a = random.randrange(n)
                if not miller_rabin_pass(a, n):
                        return False
        return True

def twinPrimes(num):
        primeList = []
        if num >= 5:
                primeList.append((3, 5))
        if num >= 7:
                primeList.append((5, 7))
        for x in xrange(0, num + 1, 30):
                if isPrime(x - 1) and isPrime(x + 1):
                        primeList.append((x - 1, x + 1))
                if isPrime(x + 11) and isPrime(x + 13) and num >= x + 13:
                        primeList.append((x + 11, x + 13))
                if isPrime(x + 17) and isPrime(x + 19) and num >= x + 19:
                        primeList.append((x + 17, x + 19))
        return primeList
    
def sieve(n):
        # Uses Sieve of Eratosthenes to generate list of primes below n
        sqrtn = int(n ** 0.5)
        sieve = [True] * (n + 1)
        sieve[0] = False
        sieve[1] = False

        for i in range(2, sqrtn + 1):
                if sieve[i]:
                        m = n // i - i
                        sieve[i*i: n + 1 :i] = [False] * (m + 1)

        sieve = [i for i in range(n+1) if sieve[i]]
        return sieve
    
def atkin(num):
        # Uses Sieve of Atkin to generate list of primes below n
        primes = [0] * (num + 1)
        if num < 2:
                return []
        if num == 2:
                return 2
        
        # n = 3x^2 + y^2
        threexSquared = 3
        for dxSquared in xrange(0, 12 * int(math.sqrt(( num - 1 ) / 3)), 24):
                threexSquared += dxSquared
                y_limit = int(12 * math.sqrt(num - threexSquared) - 36)
                n = threexSquared + 16
                for dn in xrange(-12, y_limit + 1, 72):
                        n += dn
                        primes[n] = not primes[n]
                n = threexSquared + 4
                for dn in xrange(12, y_limit + 1, 72):
                        n += dn
                        primes[n] = not primes[n]
        # n = 4x^2 + y^2
        fourxSquared = 0
        for d4xSquared in xrange(4, 8 * int(math.sqrt((num - 1 ) / 4)) + 4, 8):
                fourxSquared += d4xSquared
                n = fourxSquared + 1
                if fourxSquared % 3:
                        for dn in xrange(0, 4 * int(math.sqrt(num - fourxSquared)) - 3, 8):
                                n += dn
                                primes[n] = not primes[n]
                else:
                        y_limit = 12 * int(math.sqrt(num - fourxSquared)) - 36
                        n = fourxSquared + 25
                        for dn in xrange(-24, y_limit + 1, 72):
                                n += dn
                                primes[n] = not primes[n]
                        n = fourxSquared + 1
                        for dn in xrange(24, y_limit + 1, 72):
                                n += dn
                                primes[n] = not primes[n]
        # n = 3x^2 - y^2 section
        xSquared = 1
        for x in xrange(3, int(math.sqrt(num / 2)) + 1, 2):
                xSquared += 4 * x - 4
                n = 3 * xSquared
                if n > num:
                        min_y = ((int(math.sqrt(n - num)) >> 2) << 2)
                        ySquared = min_y * min_y
                        n -= ySquared
                        s = 4 * min_y + 4
                else:
                        s = 4
                for dn in xrange(s, 4 * x, 8):
                        n -= dn
                        if n <= num and n % 12 == 11:
                                primes[n] = not primes[n]
        xSquared = 0
        for x in xrange(2, int(math.sqrt(num / 2)) + 1, 2):
                xSquared += 4 * x - 4
                n = 3 * xSquared
                if n > num:
                        min_y = ((int(math.sqrt(n - num)) >> 2) << 2) - 1
                        yy = min_y*min_y
                        n -= yy
                        s = 4 * min_y + 4
                else:
                        n -= 1
                        s = 0
                for dn in xrange(s, 4 * x, 8):
                        n -= dn
                        if n <= num and n % 12 == 11:
                                primes[n] = not primes[n]
        # remove squares        
        for n in xrange(5, int(math.sqrt(num)) + 1, 2):
                if primes[n]:
                        for k in range(n * n, num, n * n):
                                primes[k] = False
        return [2,3] + filter(primes.__getitem__, xrange(5, num, 2))

def pi(n):
        # Returns the number of primes less than or equal to n
        return len(atkin(n))

def getFactor(n):
        # Uses Brent's version of the Pollard rho factorization method to generate one of the factors of n
        if n % 2 == 0:
                return 2
        y, c, m = random.randint(1, n - 1), random.randint(1, n - 1), random.randint(1, n - 1)
        g, r, q = 1, 1, 1
        while g == 1:             
                x = y
                for i in range(r):
                        y = ((y*y) % n + c) % n
                k = 0
                while (k < r and g == 1):
                        ys = y
                        for i in range(min(m, r - k)):
                                y = ((y*y) % n + c) % n
                                q = q * (abs(x - y)) % n
                        g = congr.gcd(q, n)
                        k = k + m
                r *= 2
        if g == n:
                while True:
                        ys = ((ys*ys) % n + c) % n
                        g = congr.gcd(abs(x - ys), n)
                        if g > 1:
                                break
         
        return g

def primeFactors(n):
        if n == 1:
                return []
        if isPrime(n):
                return [n]
        factor = getFactor(n)
        return primeFactors(factor) + primeFactors(n / factor)
        
def primeFactorization(num):
        pFactor = []
        factors = primeFactors(num)
        for fac in set(factors):
                pFactor.append((fac, factors.count(fac)))
        return pFactor

def ulamSpiral(size):
        row = size/2
        col = size/2
        direction = 0
        changeCount = -1
        count = 0
        length = 1
        spiral = [[0 for x in range(size)] for x in range(size)] 
        for a in xrange (0, size ** 2):
                spiral[row][col] = a + 1
                count += 1
                if (count == length):
                        count = 0
                        changeCount += 1
                        direction += 1
                        direction = ((direction - 1) % 4) + 1
                if (direction == 1):
                        col += 1
                elif (direction == 2):
                        row += 1
                elif (direction == 3):
                        col -= 1
                elif (direction == 4):
                        row -= 1
                if (changeCount == 2):
                        length += 1
                        changeCount = 0
        return spiral
