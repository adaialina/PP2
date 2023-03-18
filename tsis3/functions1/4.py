def isPrime(n):
    prime = []
    for i in range(a):
        for j in range(2, (int(i)//2)+1):    
            if n % j == 0:
                prime.append(i)
    print (prime)
            
answer = []
a = str(input()).split()
isPrime(a)

"""
import math

def return_primes(arr):
    return list(filter(lambda x : is_prime(x), arr))

def is_prime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

print(return_primes([10,21,3,8,9,11,44,62,100,19]))
"""