def rangeMult(arr,low,high):
    if low >= high:
        return arr
    i = low 
    j = high
    key = arr[low]
    while i < j:
        while i < j and arr[j] >= key: 
            j -=1
        arr[i] = arr[j]
        while i<j and arr[i]<= key: 
            i +=1
        arr[j] = arr[i]
    arr[j] = key
    
    rangeMult(arr,low,i-1)
    rangeMult(arr,i+1,high)
    return arr


if __name__ == "__main__":
    arr = [15,12,15,2,2,12,2,3,12,100,3,3]
    dic = {} 
    for i in arr: 
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    c = [i for i in dic]

    b = rangeMult(arr,0,len(arr)-1)
    print(b)
    
    