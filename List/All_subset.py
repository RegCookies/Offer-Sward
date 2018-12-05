def AllSubSet(str1):
    arr = []
    arr.append(str1[0:1])
    
    i=1 
    while i< len(str1):
        j = 0
        lens = len(arr)
        while j< lens:
            arr.append(arr[j]+str1[i])
            j += 1
            print("on processing")
        arr.append(str1[i]) 
        i += 1 
    return arr



if __name__ == "__main__":
    result = AllSubSet("abc")
    print(result)
