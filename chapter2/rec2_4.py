# The goal of this recipe is to get sum of cubes of two numbers within the range of 1 to 30

# find_dupl - find duplicates in a list
def find_dupl(arg):
    seen = set()
    dupl = set()
    for num in arg:
        if num in seen:
            dupl.add(num)
        else:
            seen.add(num)
    return list(dupl)

# main function
def main():
    arr = []
    arr_i = []
    arr_j = []

    for i in range(1, 31):           # include 30
        for j in range(i, 31):      # start at i to avoid duplicate unordered pairs
            s = i**3 + j**3
            arr.append(s)
            arr_i.append(i)
            arr_j.append(j)
            print(f"{i}^3 + {j}^3 = {s}")
    dup_list = find_dupl(arr)
    print("\n\n List of Ramanujan numbers between 1 and 30:")
    print(dup_list)


# Entry point
if __name__ == "__main__":
    main()

# Invoking main function
main()