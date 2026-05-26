# /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter2/rec2_3.py
# Print pyramid patterns of number 3

rows = 5

# left-aligned increasing triangle
for i in range(1, rows + 1):
    print('3 ' * i)

print("\n\n")

# right-aligned increasing triangle
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '3 ' * i)

print("\n\n")

# inverted right-shifted triangle
for i in range(1, rows + 1):
    print(' ' * (i - 1) + '3 ' * (rows + 1 - i))