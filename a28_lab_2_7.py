import sys

def leo(n):
    if n in (0, 1):
        return 1
    return leo(n - 1) + leo(n - 2) + 1

def main():
    if len(sys.argv) == 2 and (sys.argv[1]).isnumeric():
        print("here u r ", leo(int(sys.argv[1])))
    while True:  
        n = input("Enter natural number to be displayed in Leonardo's or exit to exit:")
        try:
            if n == 'exit':
                break
            else:
                print("here u r ", leo(int(n)), "\n")
        except ValueError:
            print("Enter natural number Please\n")
        
if __name__ == "__main__":
    main()
