def adjust_heap(arr,i,size):
    lchild = 2*i +1
    rchild = 2*i +2
    maxi = i
    if i < size/2:
        if lchild < size and arr[lchild] > arr[maxi]:
            maxi = lchild
        if rchild < size and arr[rchild] > arr[maxi]:
            maxi = rchild
        if maxi != i:
            arr[maxi],arr[i] = arr[i],arr[maxi]
            adjust_heap(arr,maxi,size)



def build_heap(arr,size):
    
    for i in range(size//2,0,-1):
        adjust_heap(arr,i,size) 


def heapsort(arr):
    l = len(arr) 
    build_heap(arr,l)

    
    for i in range(0,l)[::-1]:
        arr[0],arr[i] = arr[i],arr[0]
        adjust_heap(arr,0,i)
    
    return arr 
if __name__ == "__main__":
    arr = [14,22,43,56,79,1,8,10,91] 
    print(arr)
    b = heapsort(arr)
    print(b)