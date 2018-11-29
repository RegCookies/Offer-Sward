def shell_sort(arr):
    l = len(arr) 
    group = int(l/2)
    
    while group > 0 : 
        for i in range(0,group): 
            j = i + group
            while j < l: 
                k = j - group
                key = arr[j] 
                while k >= 0:
                    if arr[k] > key:
                        arr[k+group] = arr[k] 
                        arr[k] = key 
                    k -= group
                j += group
        group //= 2 
    return arr


if __name__ == "__main__":
    arr = [4,2,3,5,7,1,8,10,9] 
    print(arr)
    b = shell_sort(arr)
    print(b)