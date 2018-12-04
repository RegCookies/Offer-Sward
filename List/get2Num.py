def get2Num(arr):
    result=0
    pos = 0
    
    i = 0 
    while i < len(arr):
        result = result^arr[i]
        i +=1 
    
    tmp = result

    i = result
    
    while i&1 == 0 :
        pos += 1
        i = i >>1
    
    i =1
    while i<len(arr):
        if (arr[i] >> pos & 1 ) == 1:
            result = result^arr[i]
        i+= 1
    print(result)
    print(result^tmp)
    
if __name__ == "__main__":
    arr = [3,5,6,6,5,7,2,2]
    get2Num(arr)