def removeNestPair(s1):
    if s1 is None:
        return s1

    num_pair = 0
    s = "("
    for i in s1 :
        if i == "(":
            num_pair += 1
        elif i == ")":
            num_pair -= 1
        else: 
            s += i
    if num_pair != 0:
        return False
    else:
        s += ")" 
    return s
if __name__ == "__main__":
    s1 = "(1,2,3,(4,5),(6,7),8)"
    s2 = "(1,2,3,4,5,6,7,8"   
    print(removeNestPair(s1))
    print(removeNestPair(s2))