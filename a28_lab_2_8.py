def check(n):
    if int(n) & (int(n) - 1):
        return print("No, it's not")
    else:
        return print("Yes, it is")

n = 1
while n != 'exit':        
    print("\nEnter number to be checked or exit to exit: ")
    n = input()
    if n == 'exit':
        break
    elif not n.isnumeric():
        print("U r stupid -_-, I said number")
    else:
        check(n)
