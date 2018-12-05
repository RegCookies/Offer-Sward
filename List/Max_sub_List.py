def Max_sub_List(arr):    
    All_End = 0 
    ALL = 0
    i = 0

    while i<len(arr):
        print(All_End, All_End+arr[i],arr[i], ALL)
        All_End = max(All_End+arr[i],arr[i])
        ALL = max(ALL,All_End)
        i +=1 
    return ALL


if __name__ == "__main__":
    arr = [1,-2,4,8,-4,7,-1,-5] 
    print(Max_sub_List(arr))
    