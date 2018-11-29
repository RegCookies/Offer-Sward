def merge(left,right):
    i,j = 0,0
    result = []
    while i < len(left) and j <len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result += left[i:]
    result += right[j:] 
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    num = len(arr)//2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:]) 
    
    return merge(left,right)


if __name__ == "__main__":
    arr = [4,5,9,7,8,3,1,2]
    print(arr)
    b = merge_sort(arr) 
    print(b)     　