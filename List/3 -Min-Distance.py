def Min3(a,b,c):
    res = float("inf")
    
    temp = 0 
    i = 0
    j = 0
    k = 0
    
    while True:
        res = min(res,Max_D(a[i],b[j],c[k])) 
        temp = min(a[i],b[j],c[k])
        print(a[i],b[j],c[k],res)
        if temp == a[i]:
            i += 1 
            if i >= len(a):
                break
        elif temp == b[j]:
            j +=1
            if j >= len(b):
                break  
        else:
            k +=1 
            if k >= len(c):
                 break
    return res
    
def Max_D(a,b,c): 
    return max(abs(a-b),abs(a-c),abs(b-c))
if __name__ == "__main__":
    a = [3,4,5,7,15]
    b = [10,12,14,16,17]
    c = [20,21,23,24,37,40]
    print(Min3(a,b,c))