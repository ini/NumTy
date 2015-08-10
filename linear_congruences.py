def lcm(a, b):
        return a * b / gcd(a, b)
 
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def egcd(a, b):
    if a == 0:
        return (0, 1)
    else:
        y, x = egcd(b % a, a)
        return (x - (b // a) * y, y)
 
def modInverse(a, m):
    x, y = egcd(a, m)
    if gcd(a, m) == 1:
        return x % m
        
def incongruentSols(a, b, c):
        solutions = set()
        if (b % gcd(a, c) == 0):
                numSols = gcd(a, c);
                sol = (c + b * linearCombo(a, c)[0] / numSols) % c;
                for i in xrange(0, numSols):
                        solutions.add((sol + c * i / numSols) % c)
        return solutions
