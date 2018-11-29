def quick_sort(arr,left,right): 
    if left >= right:
        return arr
    key =  arr[left] 
    low  = left
    high = right
    
    while left<right : 
        while left < right and arr[right] >= key:
            right -=1
        arr[left] = arr[right]
        while left < right and arr[left] <= key: 
            left += 1
        arr[right] = arr[left] 
    arr[right] = key
    
    quick_sort(arr,low, left-1)
    quick_sort(arr,left+1,high)
    
    return arr



if __name__ == "__main__":
    arr = [4,5,9,7,8,3,1,2]
    print(arr)
    b = quick_sort(arr,0,len(arr)-1)
    print(b)