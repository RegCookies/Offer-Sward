def bubble_sort(R,O):
    length = len(R)
    i = 0
    c = [R[i] - O[i] for i in range(len(R))]
    for i in range(length):
        for j in range(0,length-i-1):
            if c[j] < c[j+1]:
                c[j],c[j+1] = c[j+1],c[j]
                R[j],R[j+1] = R[j+1],R[j]
                O[j],O[j+1] = O[j+1],O[j]
def judgecomplete(R,O,M):
    bubble_sort(R,O)
    print(R,O,M)
    left = M 
    length = len(R)
    i = 0
    while i < length:
        if left < R[i]:
            return False 
        else:
            left -= O[i] 
        i += 1
    return True

if __name__ == "__main__":
    R = [10,15,23,20,6,9,7,16]
    O = [2,7,8,4,5,8,6,8] 
    N = 8
    M = 50

    scheduled = judgecomplete(R,O,M) 
    
    print(scheduled)