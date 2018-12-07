def compare(s1,s2):
    dic = {} 
    
    for i in list(s1):
        if i not in dic:
            dic[i] = 1
        else: 
            dic[i] +=1
    for i in list(s2):
        if i not in dic:
            return False
        else:
            dic[i] -= 1
    
    for i in dic:
        if dic[i] != 0:
            return False
    return True

if __name__ == "__main__":
    s1 = "aaaabbc"
    s2 = "abcbaaa"
     
    flag = compare(s1,s2) 
    
    print(flag)