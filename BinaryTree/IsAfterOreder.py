def isAfterOrder(arr,start,end):
    if arr == []:
        return False

    root = arr[end] 
    i = start

    #找到第一个比root大的值 
    while i<end:
        if arr[i] > root:
            break
        i+= 1 

    # 比较是否左边全部小于root，比较是否右边全部大于root
    # 
    j = i

    while j < end: 
        if arr[j] < root :
            return False
        j+=1
    IsRightOrder = True
    
    k = 0
    while k < i :
        if arr[k] > root: 
            return False
        k+=1
    IsLeftOrder = True

    if i > start: 
        IsLeftOrder = isAfterOrder(arr,start,i-1)
    if j < end : 
        IsRightOrder = isAfterOrder(arr,i,end)
    
    return IsLeftOrder and IsRightOrder

if __name__ == "__main__":
    arr = [1,3,2,5,7,6,4]
    result = isAfterOrder(arr,0,len(arr)-1)

    print(result)        