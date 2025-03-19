# Optimized Sieve of Eratosthenes to find the nth prime
def generate_primes(nth_prime_index):
    limit = 86028126  # Estimated upper limit for 5,000,000 primes
    prime = [0] * limit
    prime[0] = prime[1] = 1  # 0 and 1 are not primes

    primes = []  # To store primes
    for i in range(2, limit):
        if prime[i] == 0:  # If 'i' is a prime
            primes.append(i)
            if len(primes) == nth_prime_index:  # Stop when we reach the nth prime
                break
            for j in range(i * i, limit, i):  # Mark multiples of 'i' as non-prime
                prime[j] = 1
    return primes

# Input and query
q = int(input())
primes = generate_primes(5000000)  # Generate primes up to the 5,000,000th prime

for _ in range(q):
    n = int(input())
    print(primes[n - 1])  # Convert to 0-based indexing
    # if 1 <= n <= len(primes):
    # else:
    #     print(f"Index {n} is out of bounds. Maximum valid index is {len(primes)}.")
