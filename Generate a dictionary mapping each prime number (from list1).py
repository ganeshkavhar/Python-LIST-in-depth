list1 = [1, 2, 3, 4, 5, 7, 11]
list2 = [3, 4, 5, 6, 7, 8, 9, 10]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Create dictionary where:
# key = prime number from list1
# value = list of (a, b) pairs from list2 where (a + b) divisible by prime
prime_divisible_pairs = {
    prime: [(a, b) for a in list2 for b in list2 if a != b and (a + b) % prime == 0]
    for prime in list1 if is_prime(prime)
}

import pprint
print("Complex dictionary of prime to pairs where sum divisible by prime:")
pprint.pprint(prime_divisible_pairs)
