def leo(n):
    if n in (0, 1):
        return 1
    return leo(n - 1) + leo(n - 2) + 1
n = 1 
while n != 'exit':  
    print("Enter natural number to be displayed in Leonardo's or exit to exit: ")
    n = input()
    if n == 'exit':
        break
    elif not n.isnumeric():
        print("U r stupid -_-, I said number")
    else:
        print("here u r ", leo(int(n)))
    print("\n\n")