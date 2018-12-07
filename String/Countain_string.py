def isCountain(s1,s2):
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        s1,s2 = s2,s1
    dic = {}
    
    for i in s1:
        if i not in dic:
            dic[i] = 1 
        else:
            dic[i] += 1 

    for i in s2:
        if i not in dic:
            return False
    return True

if __name__ == "__main__":
    s1 = "abcdef"
    s2 = 'acf'
    print(isCountain(s1,s2))


