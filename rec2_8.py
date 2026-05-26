#!/usr/bin/env python3
"""rec2_8.py — Print Fibonacci sequence for the first 10 natural numbers."""

def fib_sequence(n_terms):
    """Generate first n_terms Fibonacci numbers (F(1)=1, F(2)=1)."""
    a, b = 1, 1
    for _ in range(n_terms):
        yield a
        a, b = b, a + b

def main():
    n = 10  # first 10 natural numbers
    seq = list(fib_sequence(n))
    # Print as sequence and with indices F(1)...F(10)
    print("Fibonacci sequence (first 10 terms):")
    print(seq)
    for i, val in enumerate(seq, start=1):
        print(f"F({i}) = {val}")

if __name__ == "__main__":
    main()

#main()