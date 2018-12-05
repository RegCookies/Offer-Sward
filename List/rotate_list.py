def rotate_list(arr):
    i = len(arr) -1 
    while i>0:
        row = 0
        col = i
        while col < len(arr):
            print(arr[row][col])
            row +=1
            col +=1
        i -=1
    i = 0 
    while i < len(arr):
        row = i
        col = 0 
        while row < len(arr):
            print(arr[row][col])
            row +=1
            col +=1
        i +=1

if __name__ == "__main__":
    arr = [[1,2,3],[4,5,6],[7,8,9]]
    rotate_list(arr)