
def insert_sort(arr): 
    l = len(arr)
    print(l)
    for i in range(1,l):
        keyx = arr[i]
        j = i-1
        while j>=0:
            if arr[j] > keyx:
                arr[j+1] = arr[j]
                arr[j] = keyx 
            j -= 1
    return arr 
if __name__ == "__main__":
    arr =  [2,1,3,5,7,6,9,10,15,11]
    b = insert_sort(arr) 
    print(b)   