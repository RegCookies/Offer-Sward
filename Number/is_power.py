def ispower(n):
    low = 1
    high = n
    while low < high:
        mid = (low + high)//2
        power = mid * mid 
        if power > n:
            high = mid - 1
        elif power < n:
            low = mid +1
        else:
            return True 
    return False
if __name__ == "__main__":
    n1 = 15
    n2 = 16 
    print(ispower(n1))
    print(ispower(n2))