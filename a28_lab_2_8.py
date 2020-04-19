def check(n):
    if int(n) & (int(n) - 1):
        return print("No, it's not")
    else:
        return print("Yes, it is")

def main():
    while True:        
        n = input("\nEnter number to be checked or exit to exit: ")
        try:
            if n == 'exit':
                break
            elif not n.isnumeric():
                print("U r stupid -_-, I said number")
            else:
                check(n)
        except ValueError:
            print("Enter natural number Please")

if __name__ == "__main__":
    main()