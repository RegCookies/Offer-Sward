def Missing(arr):
    suma = 0
    sumb = 0
    i = 0
    while i<len(arr): 
        suma += arr[i]
        sumb += i
        i +=1
    print(sumb)
    sumb = sumb + len(arr) + len(arr) + 1

    return sumb - suma 

if __name__ == "__main__":
    arr = [2,1,4,3,5,7]
    print(Missing(arr))