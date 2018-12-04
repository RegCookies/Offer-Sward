def getMin_R(arr,low,high):
    if high < low:
        return arr[0]
    if high == low:
        return arr[low] 
        
    mid = (low + high)//2
    
    if arr[mid] < arr[mid-1]: 
        return arr[mid] 
    elif arr[mid+1] < arr[mid]: 
        return arr[mid+1] 
    elif arr[high] > arr[mid]:
        return getMin_R(arr,low,mid-1)
    elif arr[low]< arr[mid]:
        return getMin_R(arr,mid+1,high) 
    else:
        return min(getMin_R(arr,low,mid-1), getMin_R(arr,mid+1,high))


if __name__ == "__main__":
    arr = [5,6,1,2,3,4]
    
    mins  =getMin_R(arr,0,len(arr)-1)
    print(mins)
