def bubble(arr):
    l = len(arr)
    c = 0
    for i in range(l-1):
        c = 0
        for j in range(0,l-1-i):
            print(i,j,arr[i],arr[j]) 
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
            c+=1
        if 0== c: 
            break
    print(c)
    return arr 

if __name__ == "__main__":
    arr = [4,5,9,7,8,3,1,2]

    b = bubble(arr) 
    print(b) 