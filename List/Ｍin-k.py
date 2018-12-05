def find_Min(arr,k,low,high):
    if low >= high:
        return arr
    i = low
    j = high
    
    key = arr[i]
    
    while i< j:
        while i<j and arr[j] >= key:
            j -=1
        arr[i] = arr[j] 
        while i<j and arr[i] <= key:
            i +=1
        arr[j] = arr[i]
    arr[j] = key 
    find_Min(arr,k,low,i-1)
    find_Min(arr,k,i+1,high)
    
    return arr[k-1]

def find_Min1(arr,k,low,high):
    if low >= high:
        return arr
    i = low
    j = high
    key = arr[i]
    while i< j:
        while i<j and arr[j] >= key:
            j -=1
        arr[i] = arr[j] 
        while i<j and arr[i] <= key:
            i +=1
        arr[j] = arr[i]
    arr[j] = key 
    sub = i - low
    if sub == k-1:
        return arr[i]
    elif sub > k-1:
        return find_Min1(arr,k,low,i-1) 
    else: 
        return find_Min1(arr,k, k-(i-low)-1,high) 
if __name__ == "__main__":
    arr = [4,0,1,0,2,3]
    k = 3 
    print(find_Min1(arr,k,0,len(arr)-1))