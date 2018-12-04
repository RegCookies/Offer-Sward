def findDup(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i] = 1
        else: 
            return i

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,1] 
    b = findDup(arr) 
    print(b)
     
            