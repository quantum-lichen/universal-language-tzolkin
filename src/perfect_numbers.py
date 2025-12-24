"""
Perfect Number Utilities

Mathematical functions for working with perfect numbers,
Mersenne primes, and related number theory.
"""

from typing import List, Tuple
import math


# Known perfect numbers
PERFECT_NUMBERS = [6, 28, 496, 8128, 33550336, 8589869056]

# Known Mersenne primes (2^p - 1)
MERSENNE_PRIMES = [3, 7, 31, 127, 8191, 131071]


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_of_divisors(n: int) -> int:
    """Calculate sum of all divisors of n (including n itself)."""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors)


def is_perfect(n: int) -> bool:
    """
    Check if a number is perfect.
    
    A perfect number equals the sum of its proper divisors.
    Equivalently: σ(n) = 2n where σ is sum of all divisors.
    """
    return sum_of_divisors(n) == 2 * n


def get_divisors(n: int) -> List[int]:
    """Get all divisors of n (excluding n itself)."""
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != 1 and i != n // i and n // i != n:
                divisors.append(n // i)
    return sorted(divisors)


def euler_formula(p: int) -> int:
    """
    Generate perfect number using Euler's formula.
    
    N = 2^(p-1) × (2^p - 1)
    
    Returns perfect number if both p and (2^p - 1) are prime.
    """
    if not is_prime(p):
        raise ValueError(f"{p} is not prime")
    
    mersenne = 2**p - 1
    if not is_prime(mersenne):
        raise ValueError(f"2^{p} - 1 = {mersenne} is not prime")
    
    return 2**(p-1) * mersenne


def verify_perfect(n: int) -> Tuple[bool, str]:
    """
    Verify if a number is perfect and explain why.
    
    Returns:
        (is_perfect, explanation)
    """
    divisors = get_divisors(n)
    divisor_sum = sum(divisors)
    
    if divisor_sum == n:
        return (True, f"{n} is perfect: {' + '.join(map(str, divisors))} = {n}")
    else:
        return (False, f"{n} is not perfect: {' + '.join(map(str, divisors))} = {divisor_sum} ≠ {n}")


if __name__ == "__main__":
    print("Perfect Numbers Test")
    print("=" * 50)
    
    # Test known perfect numbers
    for n in PERFECT_NUMBERS[:4]:  # Test first 4
        is_perf, explanation = verify_perfect(n)
        print(f"✓ {explanation}")
    
    print()
    print("Testing Euler's formula:")
    for p in [2, 3, 5, 7]:
        try:
            n = euler_formula(p)
            print(f"p={p}: 2^{p-1} × (2^{p} - 1) = {n} ✓")
        except ValueError as e:
            print(f"p={p}: {e}")
