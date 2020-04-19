def to_obj(json):
    
    if json[0] == '{':
        res, st_elem, a_braket, b_braket, word, temp = {}, 1, -1, -1, -1, []
       
        for i in range(1, json.__len__() - 1):
            if json[i] == '"': 
                word *= -1  
            elif (json[i] == '[' or json[i] == ']') and word == -1:  
                a_braket *= -1  
            elif (json[i] == '{' or json[i] == '}') and word == -1: 
                b_braket *= -1 
                
            if json[i] == ',' and word == a_braket == b_braket == -1:
                temp.append(json[st_elem:i])  
                st_elem = i + 2 
                
            if i == json.__len__() - 2:  
                temp.append(json[st_elem:i + 1]) 
                print(temp)
                
        for k in temp:  
            key, value = k.split(':')
            res[key[1:key.__len__()-1 ]] = to_obj(value[1: value.__len__()])
        return res
    
    elif json[0] == '[': 
        res, st_elem, a_braket, b_braket, word = [], 1, -1, -1, -1 
        
        for i in range(1, json.__len__() - 1):
            if word == a_braket == b_braket == -1 and json[i] == ',':
                res.append(to_obj(json[st_elem:i])) 
                st_elem = i + 2
                
            if i == json.__len__() - 2:
                res.append(to_obj(json[st_elem:i + 1]))
                
            if json[i] == '"':
                word *= -1
            elif (json[i] == '[' or json[i] == ']') and word == -1:
                a_braket *= -1
            elif (json[i] == '{' or json[i] == '}') and word == -1:
                b_braket *= -1
        return res
    
    elif json[0] == '"':  
        return json[1:json.__len__() - 1] 
    elif json == 'true':
        return True
    elif json == 'false':
        return False
    elif json == 'null':
        return None
    elif json.__contains__('.'):  
        return float(json)
    else:
        return int(json)  


def main():
    while True:
        try:
            choose = int(input("Enter 1 to read from file\n2 to enter manually"
                               "\n3 to exit\n"))
            break
        except ValueError:
            print("You must input integer number")
            
        if choose not in range(1,3):
            print("Number must be 0 or 1 or 2")
            
    if choose == 1:
        f = open('to_obj.txt', 'r')
        JSON = f.readline()
        f.close()
    elif choose == 2:
        JSON = input("Input your string in JSON\n")
    elif choose == 3:
        exit()
    obj = to_obj(JSON)
    print(obj)

if __name__ == "__main__":
    main()