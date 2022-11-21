from math import *

def is_prime(num, i):
    if i == 1:
        return True
    elif num == i:
        return is_prime(num, i - 1)
    elif num % i != 0:
        return is_prime(num, i - 1)

def all_primes_f():
    global all_primes
    all_primes = []
    for i in range(2, 150):
        if is_prime(i, i):
            all_primes.append(i)
    return all_primes

def all_primes_cond_f():
    global all_primes_N
    all_primes_N = []
    all_primes_f()
    for x in all_primes:
        for j in range(len(all_primes)):
            if 4 * j + 1 == x:
                all_primes_N.append(x)
    return all_primes_N

print('all primes < 150:', all_primes_f())
print('all primes form 4k+1 < 150:', all_primes_cond_f())

def sum_all_a(aa, bb):
    global Ns
    Ns = []
    i = 0
    ctr_a = 0
    while i < aa:
        j = 0
        while j < bb:
            if i <= j:
                for prime in all_primes_N:
                    N = pow(i, 2) + pow(j, 2)
                    if sqrt(N).is_integer() == False and N % prime == 0:
                        print("a =", i, "  b =", j, " prime =", prime, "        N = ", N)
                        ctr_a += i
                        break
            j += 1
        i += 1
    print("the sum =", ctr_a)

a, b = int(input("max value for a: ")), int(input("max value for b: "))
sum_all_a(a, b)           