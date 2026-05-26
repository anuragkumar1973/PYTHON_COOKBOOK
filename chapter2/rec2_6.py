# Recipe2.7.1 Using inline lambda functions in nested for loops and comprehensions
print("\n Recipe 2.7.1:")
evens = [n for _ in [None] for n in range(1, 6) if (lambda x: x % 2 == 0)(n)]
print(evens)  # -> [2, 4]

# Recipe 2.7.2 - simpler one-line version (outer loop removed)
print("\n Recipe 2.7.2:")
evens = [n for n in range(1, 6) if (lambda x: x % 2 == 0)(n)]
print(evens)  # -> [2, 4]

# Recipe 2.7.3 - inline lambda called inside a for-loop to format and categorize each city

# Explanation:
# Iterates over `cities` (a mapping of city -> number of Python experts).
# For each (city, count) pair it prints a single line like:
#   "CityName: 120000 Python experts - very high"
# The printed string is built by an inline lambda that returns an f-string.
# The severity label is chosen with a chained conditional expression:
#   - "very high" when n > 100_000
#   - "high" when 50_000 <= n <= 100_000
#   - "moderate" otherwise
print("\n Recipe 2.7.3:")
cities = {
    "Dallas": 20000,
    "Delhi": 200000,
    "Los Angeles": 45000,
    "Seattle": 80000,
}
for city, count in cities.items():
    print((lambda name, n: f"{name}: {n} Python experts - "
                          f"{'very high' if n > 100_000 else 'high' if n >= 50_000 else 'moderate'}")
          (city, count))

# Recipe 2.7.4 - same as above but without lambda
print("\n Recipe 2.7.4:")
for city, count in cities.items():
    print(f"{city}: {count} Python experts - "
          f"{'very high' if count > 100_000 else 'high' if count >= 50_000 else 'moderate'}")
