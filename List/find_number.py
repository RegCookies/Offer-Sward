def find_number(arr,n):
    i = 0 
    rows = len(arr) 
    cols = len(arr[i]) 
    j = cols -1 

    while i < rows and j >= 0 :
        if arr[i][j] == n:
            return True 
        elif arr[i][j] > n:
            j -= 1
        else:
            i +=1
    return False
if __name__ == "__main__":
    arr = [[1,2,3,4,5],[10,11,12,13,14],[21,22,23,24,25],[31,32,33,34,35]]
    print(find_number(arr,14)) 
    
