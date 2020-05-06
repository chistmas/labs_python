import sys

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
    
def flatten_it(y):
    for x in y:
        if x == y:
            raise ValueError
        if hasattr(x, '__iter__') and not isinstance(x, str):  
            yield from flatten_it(x)  
        else:
            if isinstance(x, int) or isinstance(x, float):
                yield x
            elif x.isnumeric():
                yield int(x)
            elif isfloat(x):
                yield float(x)
            else:
                yield x


def main():
    obj = []
    if len(sys.argv) > 1:
        obj =sys.argv[1::] 
        new = []
        for i in obj:
            i = i.replace("[", "")
            i = i.replace("]", "")
            i = i.replace(",", "")
            new.append(i)
    else:
        new = [1,[2.3,[3,4,5]],6,[7,8],9,["a",[11,12,[13,[14,15]]]]]
        new[0] = new 
    try:
        print(list(flatten_it(new)))
    except ValueError: 
        print('Array that refers to itself')


if __name__ == "__main__":
    main()
