# rec2_1.py - iterate/unpack common data types
# Examples of unpacking lists, dictionaries, tuples, and sets.

def main():
    # 1. Unpacking a List
    tasks = ["email", "report", "meeting"]
    print("Unpacking list:")
    for task in tasks:
        print(task)

    # 2. Unpacking a Dictionary
    config = {"timeout": 30, "retry": 3}
    print("\nUnpacking dictionary:")
    for key, value in config.items():
        print(f"{key}: {value}")

    # 3. Unpacking a Tuple
    coordinates = (10, 20)
    print("\nUnpacking tuple (iterating):")
    for coord in coordinates:
        print(coord)
    # direct unpack
    x, y = coordinates
    print(f"Direct unpack: x={x}, y={y}")

    # 4. Unpacking a Set
    unique_ids = set([101, 102, 103])
    print("\nUnpacking set:")
    for uid in unique_ids:
        print(uid)

if __name__ == "__main__":
    main()

main()