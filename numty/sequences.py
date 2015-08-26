# -*- coding: utf-8 -*-
from fractions import Fraction as Fr
import primes as ps
import multFunc as mf
import math

def additiveSequence(n, t0, t1):
        # Returns nth member of the sequence t0, t1, t0+t1, t1+t2, t2+t3, ...
        if n == 0:
                return t0
        if n == 1:
                return t1
        try:
                return additiveSequence(n - 1, t1, t0 + t1)
        except:
                return "Error: Number is too large."
        
def fibonacci(n):
        return additiveSequence(n, 0, 1)
        
def polygonal(sides, n):
        return (n*n*(sides - 2) - n*(sides - 4)) / 2
        
def triangle(n):
        return polygonal(3, n)
        
def square(n):
        return n * n

def pentagon(n):
        return polygonal(5, n)
        
def abundant(n):
        # Returns the nth natural number less than the sum of its proper divisors
        count = 0
        num = 0
        while count < n:
                num += 1
                if mf.sigma(num) > 2 * num:
                        count += 1
        return num
        
def deficient(n):
        # Returns the nth natural number less than the sum of its proper divisors
        count = 0
        num = 0
        while count < n:
                num += 1
                if mf.sigma(num) < 2 * num:
                        count += 1
        return num
        
def aliquot(k, n):
        # Returns the nth member of the sequence defined by {s_0 = k, s_n = σ(s_n−1) − s_n−1}
        if n == 0:
                return k
        return mf.sigma(aliquot(k, n - 1)) - aliquot(k, n - 1)
        
def lookAndSay(n):
        if n < 1:
                return ""
        if n == 1:
                return "1"
        if n == 2:
                return "11"
        oldStr = lookAndSay(n - 1)
        newStr = ""
        prevChar = oldStr[0]
        count = 1
        for i in xrange(1, len(oldStr)):
                if oldStr[i] == prevChar:
                        count += 1
                else:
                        newStr += str(count) + prevChar
                        prevChar = oldStr[i]
                        count = 1
        newStr += str(count) + prevChar
        return newStr

def prime(n):
        # Returns the nth prime
        if n == 1 or n == 2:
                return n + 1
        
        upperBound = n
        for i in xrange(0, 20):
                # Uses Newton's Method to approximate an upper bound, given n = pi(x) > x/lnx 
                f = 1 * upperBound / math.log(upperBound) - n
                f_deriv = (math.log(upperBound) - 1) / (math.log(upperBound) ** 2)
                upperBound -= f / f_deriv
        return ps.sieve(int(math.ceil(upperBound)))[n - 1]

def catalan(n):
        product = 1
        for k in xrange(2, n + 1):
                product *= (n + k) / float(k)
        return product
 
def bernoulli(n):
        # Uses Akiyama–Tanigawa algorithm to calculate nth Bernoulli number
        if n % 2 == 1 and n > 3:
                return 0
        A = [0] * (n + 1)
        for m in range(n + 1):
                A[m] = Fr(1, m + 1)
                for j in range(m, 0, -1):
                        A[j - 1] = j * (A[j - 1] - A[j])
        return A[0]
