def find_MM(arr,left,right):
    if left >= right:
        return arr 
    key = arr[left]

    while left <= right:
        while left < right and arr[left] < key:
            left += 1
        arr[right] = arr[left]
        while left< right and arr[right] > key:
            right -= 1
        arr[left] = arr[right] 
    arr[right] = key

    return arr,arr
    

if __name__ == "__main__":
    arr = [3,1,2,4,5,7,6,9]
    a,b = find_MM(arr,0,len(arr)-1)
    print(a,b)