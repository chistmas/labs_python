def to_JSON(obj):
    res = ''
    if obj is None:
        return "null"
    elif type(obj) == list or type(obj) == tuple:
        res += '['  
        for i in range(obj.__len__()):  
            res += to_JSON(obj[i])   
            if i < obj.__len__() - 1:  
                res += ', '
        res += ']'
    elif type(obj) == dict:
        res += '{'
        count = 0 
        for key, value in obj.items():  
            res += '"' + key + '": ' + to_JSON(value)
            if count < obj.__len__() - 1:
                res += ', '
            count += 1
        res += '}'
    elif type(obj) == int or type(obj) == float:
        return str(obj)
    elif type(obj) == str:
        return '"' + obj + '"'
    elif type(obj) == bool:
        return str(obj).lower()
    else:
        raise ValueError
    return res


def main():
    x = {"name": "Tim","age": 18,"city": "Minsk", 
             "array": [5, 1.2, True, "faag"], "dictionary": {"first": 1,
                      "second": 'asdv', "third": ['sryh', 6, False],
                      "fourth": (True, 67, [98, 54, 'hfsdjkhfkds', {
                              "firstElement": '1', "secondElement": 2,
                              "thirdElement": [45,'sdvs',
                                               (45, 78.95, False, 'fjhdskf')]
                              }]),},"zero": None}    
    while True:
        try:
            choose = int(input("Enter 1 to write into file\n"
                               "2 to print into console\n3 to exit"))
            break
        except ValueError:
            print("You must input integer number")
        if choose != 1 and choose != 2 and choose != 3:
            print("Number must be 1 or 2 or 3")
    if choose == 1:
        f = open('result.txt', 'w')
        f.write(to_JSON(x))
        f.close()
    elif choose == 2:
        print(to_JSON(x))
    else:
        print("See you later\n")


if __name__ == "__main__":
    main()