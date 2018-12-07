def getMaxSubString(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    maxS = 0
    maxI = 0 
    matrix = [[0]*(l1+1) for i in range(l2+1)] 
    
    i =1 
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if arr1[i-1] == arr2[j-1]:
                matrix[i][j] = matrix[i-1][j-1] + 1
                if matrix[i][j] > maxS:
                    maxS = matrix[i][j] 
                    maxI = i
    print(maxS,maxI)
    return ''.join(arr1[maxI-1:maxS-1:-1])
                 

if __name__ == "__main__":
    arr1 = "abccade"
    arr2 = "dgcadde"
    print(getMaxSubString(list(arr1),list(arr2)))