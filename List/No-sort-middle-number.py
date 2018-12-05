class Test:
    def __init__(self): 
        self.pos = 0
    def pos12(self,arr,low,high):
        i = low
        j = high
        key = arr[low]
        while i<j:
            while i<j and arr[j] >= key:
                j -= 1
            arr[i] = arr[j]
            while i<j and arr[i] <= key:
                i += 1
            arr[j] = arr[i] 
        arr[j] = key
        return j

    def NoSortMiddleNumber(self,arr):
        low = 0
        high = len(arr)-1
        mid  = (low + high) //2
        while True:
            
            pos = self.pos12(arr,low,high)
            if pos == mid:
                break

            elif pos > mid:
                high = pos - 1
            else:
                low = pos +1 
            print(mid,arr[mid],arr[mid+1])
            print(low,high)
        return arr[mid] if (len(arr)%2 != 0) else (arr[mid]+ arr[mid+1])/2
    

if __name__ == "__main__":
    arr = [7,5,3,1,11,9]
    print(Test().NoSortMiddleNumber(arr))