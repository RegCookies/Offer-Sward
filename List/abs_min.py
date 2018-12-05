def absMin(arr): 
    if arr[0] >0:
        return arr[0]
    if arr[-1] <0:
        return arr[-1] 
    
    low = 0
    high = len(arr)
    
    while low < high: 
        mid = (low + high)//2
        if arr[mid] == 0:
            return 0 
        elif arr[mid] >0:
            if arr[mid-1] <= 0:
                return min(abs(arr[mid]),abs(arr[mid-1])) 
            
            else:
                high = mid
        elif arr[mid] < 0: 
            if arr[mid+1] >= 0:
                return min(abs(arr[mid]),abs(arr[mid+1]))
            else:
                low = mid
    


if __name__ == "__main__":
    arr = [-10,-5,-2,7,15,50] 
    print (absMin(arr))