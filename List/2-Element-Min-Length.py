def MinLength(arr,num1,num2):
    res = float('inf')
    last1  = -1
    last2  = -1
    i = 0
    while i< len(arr):
        if arr[i] == num1:
            last1 = i
            if last2 >= 0:
                print(last1,last2)
                res = min(res,abs(last2-last1))
        if arr[i] == num2:
            last2 = i
            if last1 >= 0 : 
                print(last1,last2)
                res = min(res,abs(last2-last1)) 
        i +=1  
    return res


if __name__ == "__main__":
    arr = [4,5,6,4,7,4,6,4,7,8,5,6,4,3,10,8]
    num1 = 4
    num2 = 8 
    print(MinLength(arr,num1,num2))