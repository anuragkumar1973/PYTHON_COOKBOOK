# /Users/anuragkumar1973/Downloads/book_py_cookbk/chapter2/rec2_2.py

add = lambda x, y: x + y
add_sqrd= lambda x, y: x**2 + y**2

xs = range(0, 6)    # 0 to 5 inclusive
ys = range(-5, 1)   # -5 to 0 inclusive

# Pairwise addition (0 with -5, 1 with -4, ..., 5 with 0)
for x, y in zip(xs, ys):
    print(f"{x} + {y} = {add(x, y)}")
print("\n")

for x, y in zip(xs, ys):
    print(f"{x}^2 + {y}^2 = {add_sqrd(x, y)}")
print("\n")