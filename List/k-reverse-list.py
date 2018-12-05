def kreverse(arr,k):
    return arr[k:] + arr[:k]

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    print(kreverse(arr,4))