def find_max_cover(arr,n):
    i = 0
    j = 1
    n = len(arr)
    count =0
    maxCount = 0
    while i<len(arr) and j < len(arr): 
        while j< n and arr[j] - arr[i] <= n:
            j +=1
            count += 1
        # j 回退 
        j -= 1
        count -= 1
        if maxCount < count:
            start =  i
            maxCount = max(count,maxCount)  
        i += 1
        j += 1
    print(i,maxCount)
    return arr[start:start+maxCount-1]       
if __name__ == "__main__":
    arr= [1,3,7,8,10,11,12,13,15,16,17,19,25] 
    print(find_max_cover(arr,8))