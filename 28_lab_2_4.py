import sys

def isfloat(value):
  try:
    float(value)
    return True
  except ValueError:
    return False

def flatten_it(lis):
    c = []
    che = True        
    for i in lis:
        if isinstance(i, list):
            t = True
            while t:
                t = 0
                for j in i:
                    if isinstance(j, list) and len(j) > 1:
                        i = j
                        t= 1
                    else:
                        if isinstance(j, str):
                            che = False
                        else:
                            c.append(j)
        elif isinstance(i, str):
            b = i.replace("[", "")
            b = b.replace("]", "")
            b = b.replace(",", "")
            if b.isnumeric():
                c.append(int(b))
            elif isfloat(b):
                c.append(float(b))
            else:
                che = False
        else:
            c.append(i)
        lis = c
    if che:
        print(lis)
    else:
        print("There's initterable in list")
"""            elif isinstance(i, float):
                c.append(i)
                print(3)
            else:
                print(4)
                c.append(i)
"""
        
"""    if che:
        print(lis)
    else:
        print("There's initterable in list")"""
'''c = []
    che = True
    for i in a:
        if i.isnumeric():
            c.append(int(i))
        elif isfloat(i):
            c.append(float(i))
        else:
            che = False
    if che:
        print(c)
    else:
        print("There's initterable in list")'''

if len(sys.argv) > 1:
    sist = sys.argv[1::]
flatten_it(sist)