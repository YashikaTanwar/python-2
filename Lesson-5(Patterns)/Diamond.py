for i in range(1, 6, 2):
    print(" " * ((5 - i) // 2), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(3, 0, -2):
    print(" " * ((5 - i) // 2), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()