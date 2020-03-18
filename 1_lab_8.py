print("Enter number to be checked: ")
n = input()
if not n.isnumeric():
    print("U r stupid -_-, I said number")
elif int(n) & (int(n) - 1) :
    print("No, it's not")
else:
    print("Yes, it is")
