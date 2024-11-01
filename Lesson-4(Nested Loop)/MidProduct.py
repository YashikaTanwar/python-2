num = input("Enter a number: ")
numlen = len(num)

if numlen % 2 == 0:
    # For even-length numbers, get the two middle digits
    mid1 = int(num[numlen // 2 - 1])
    mid2 = int(num[numlen // 2])
    prod = mid1 * mid2
    print("Product of the middle digits:", prod)
else:
    # For odd-length numbers, get the middle digit and square it
    mid = int(num[numlen // 2])
    prod = mid * mid
    print("Square of the middle digit:", prod)
