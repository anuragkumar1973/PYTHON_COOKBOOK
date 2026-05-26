#!/usr/bin/env python3
"""Example: iterate through a dictionary of cities and software engineer populations."""

def main():
    engineers = {
        "Dallas": 15000,
        "Delhi": 200000,
        "Los Angeles": 50000,
    }

    print("Software engineers by city:")
    for city, count in engineers.items():
        print(f" - {city}: {count:,} engineers")

if __name__ == "__main__":
    main()

main