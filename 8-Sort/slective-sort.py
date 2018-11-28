def selevtive_sort(arr):
    l = len(arr)
    for i in range(l):
        min1 = i
        for j in range(i+1,l):
            if arr[min1] > arr[j]:
                 min1 = j
        arr[i],arr[min1] = arr[min1], arr[i]
    return arr
    

if __name__ == "__main__":
    arr =[2,3,5,6,8,1,7,10]

    b = selevtive_sort(arr)
    print(b)    