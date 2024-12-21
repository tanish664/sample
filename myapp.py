def find_primes(n):
    """
    Find all prime numbers up to n using the Sieve of Eratosthenes algorithm.
    
    Args:
    n (int): Upper limit for finding prime numbers
    
    Returns:
    list: A list of prime numbers less than or equal to n
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
   
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    
    # Collect and return all prime numbers
    return [num for num in range(2, n + 1) if is_prime[num]]

# Example usage
def main():
    limit = 50
    primes = find_primes(limit)
    print(f"Prime numbers up to {limit}:")
    print(primes)
    
    # Additional demonstration of prime number properties
    print(f"\nTotal number of primes found: {len(primes)}")
    print(f"Largest prime found: {primes[-1]}")

if __name__ == "__main__":
    main()
