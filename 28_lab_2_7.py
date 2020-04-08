import sys
def leo(n):
    if n in (0, 1):
        return 1
    return leo(n - 1) + leo(n - 2) + 1
n = 1 
if len(sys.argv) == 2 and (sys.argv[1]).isnumeric():
    print("here u r ", leo(int(sys.argv[1])))
while n != 'exit':  
    print("Enter natural number, "
          "or arg to be displayed in Leonardo's or exit to exit: ")
    n = input()
    if n == 'exit':
        break
    elif n == 'arg':
        if len(sys.argv) == 2 and (sys.argv[1]).isnumeric():
            print("here u r", leo(int(sys.argv[1])))
        else: print("there is no int in arg")
    elif not n.isnumeric():
        print("U r stupid -_-, I said number")
    
    else:
        print("here u r ", leo(int(n)))
    print("\n")
