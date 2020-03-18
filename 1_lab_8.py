print("Enter number to be checked: ")
n = int(input())
if type(n) != int:
    print("U r stupid -_-")
if n & (n - 1) :
    print("No, it's not")
else:
    print("Yes, it is")
