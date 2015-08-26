import primes as py

def lcm(a, b):
        return a * b / gcd(a, b)
 
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

# Returns two integers x, y such that gcd(a, b) = ax + by
def egcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        y, x = egcd(b % a, a)
        return (x - (b // a) * y, y)

# Returns an integer x such that ax = 1(mod m)
def modInverse(a, m):
    x, y = egcd(a, m)
    if gcd(a, m) == 1:
        return x % m

# Reduces linear congruence to form x = b(mod m)
def reduceCongr(a, b, m):
        gcdAB = gcd(a, b)
        a /= gcdAB
        b /= gcdAB
        m /= gcd(gcdAB, m)
        modinv = modInverse(a, m)
        b *= modinv
        return (1, b, m)
        
# Returns the incongruent solutions to the linear congruence ax = b(mod m)
def linCongr(a, b, m):
        solutions = set()
        if (b % gcd(a, m) == 0):
                numSols = gcd(a, m)
                sol = (b * egcd(a, m)[0] / numSols) % m
                for i in xrange(0, numSols):
                        solutions.add((sol + m * i / numSols) % m)
        return solutions

# Uses the Chinese Remainder Theorem to solve a system of linear congruences
def crt(congruences):
        x = 0
        M = 1
        for i in xrange(len(congruences)):
                M *= congruences[i][2]
                congruences[i] = reduceCongr(congruences[i][0], congruences[i][1], congruences[i][2])

        for j in xrange(len(congruences)):
                m = congruences[j][2]
                if gcd(m, M/m) != 1:
                        return None
                x += congruences[j][1] * modInverse(M/m, m) * M / m

        return x % M

# Returns the incongruent solution to any system of linear congruences
def linCongrSystem(congruences):
        newCongruences = []
        for i in xrange(len(congruences)):
                congruences[i] = reduceCongr(congruences[i][0], congruences[i][1], congruences[i][2])
                
                # Tests to see whether the system is solvable
                for j in xrange(len(congruences)):
                        if congruences[i] != congruences[j]:
                                if (congruences[i][1] - congruences[j][1]) % gcd(congruences[i][2], congruences[j][2]) != 0:
                                        return None
                
                # Splits moduli into prime powers
                pFactor = py.primeFactorization(congruences[i][2])
                for term in pFactor:
                        newCongruences.append((1, congruences[i][1], term[0] ** term[1]))

        # Discards redundant congruences
        newCongruences = sorted(newCongruences, key=lambda x: x[2], reverse = True)
        finalCongruences = []
        for k in xrange(len(newCongruences)):
                isRedundant = False
                for l in xrange(0, k):
                        if newCongruences[l][2] % newCongruences[k][2] == 0:
                                isRedundant = True
                if not isRedundant:
                        finalCongruences.append(newCongruences[k])

        return crt(finalCongruences)

# Returns incongruents solutions to a polynomial congruence
def polyCongr(coefficients, m):
        solutions = []
        for i in xrange(m):
                value = 0
                for degree in xrange(len(coefficients)):
                        value += coefficients[degree] * (i ** (len(coefficients) - degree - 1))
                if value % m == 0:
                        solutions.append(i)

        return solutions


