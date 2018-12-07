def All_permutation(arr,start):
    if arr is None and start<0:
        return 
    if start == len(arr)-1:
        print("".join(arr))
    else:
        i = start
        while i< len(arr): 
            arr[start],arr[i] = arr[i],arr[start]
            All_permutation(arr,start+1)
            arr[start],arr[i] = arr[i],arr[start]
            i+=1


if __name__ == "__main__":
    arr = "abc"
    All_permutation(list(arr),0)