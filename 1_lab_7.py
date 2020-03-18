def leo(n):
    if n in (0, 1):
        return 1
    return leo(n - 1) + leo(n - 2) + 1
    
print("Enter the number to be displayed in Leonardo's: ")
n = input()
if not n.isnumeric():
    print("U r stupid -_-, I said number")
else:
    print(leo(int(n)))
