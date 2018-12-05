def isOne(n,i):
    return (n&(1<<i)) == 1 
    

def findSingle(arr):
    size = len(arr)
    i = 0
    
    while i<32:
        result1 = result0 = count0 = count1 = 0
        j =0
        
        while j < size:
            if isOne(arr[j],i):
                result1 ^= arr[j]
                print(result1,arr[j],i)
                count1 +=1
            else : 
                result0 ^= arr[j]
                print(result0,arr[j],i,"统计０的位数")
                count0 += 1
            j +=1
        i +=1
    
        print(count1,count0,result0,result1)
        if count1 % 2 == 1 and result0 != 0:
            return result1
    
        if count0 % 2  == 1 and result1 != 0:
            return result0
    return -1
if __name__ == "__main__":
    arr = [6,3,4,5,9,4,3] 
    result = findSingle(arr)
    if result != -1:
        print(result)