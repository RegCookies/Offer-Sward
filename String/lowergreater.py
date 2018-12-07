def lower(s1):
    low = 0
    high = len(s1)-1
    while low < high:
        while low < high and s1[low] >= "a" and s1[low] <= "z":
            low +=1
        while low < high and s1[high] >= "A" and s1[high] <= "Z":
            high -=1
        s1[low],s1[high] = s1[high],s1[low]
    return s1
if __name__ == "__main__":
    s1 = "AFECacbd"
    print(lower(list(s1)))