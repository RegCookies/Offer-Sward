class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second

def findPair(arr): 
    i = 0
    n = len(arr)
    s = {}
    
    while i<n:
        j = i+1
        while j < n:
            sumP = arr[i] + arr[j]
            if sumP not in s: 
                s[sumP] = Pair(i,j)
            else:
                p = s[sumP]
                print(arr[p.first],arr[p.second],arr[i],arr[j]) 
            j +=1
        i +=1

if __name__ == "__main__":
    arr = [3,4,7,10,20,9,8]
    findPair(arr)   