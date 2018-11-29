import math
def radix_sort(arr):
#先找这是几位数
    radix = 10
    k = int(math.ceil(math.log(max(arr),radix)))
    bucket =[[] for i in range(radix)]
    
    for i in range(1,k+1):
        for j in arr: 
            print(j//(radix**(i-1))%(radix**i),(radix**(i-1))%(radix**i))
            bucket[j//(radix**(i-1))%(radix**i)].append(j) 
        del arr[:]
        for z in bucket :
            arr += z
            del z[:]

    return arr

if __name__ == "__main__":
    arr = [14,22,43,56,79,1,8,10,91] 
    print(arr)
    b = radix_sort(arr)
    print(b)