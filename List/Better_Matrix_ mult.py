def MatrixChainOrder(p,n):
    cost = [[0]* n for i in range(n)]
    i = 1
    Clen = 2 
    while Clen < n:
        i = 1
        while i < n - Clen + 1:
            j = i + Clen - 1
            cost[i][j] = float("inf")
            k = i
            while k <= j-1:
                q = cost[i][k] + cost[k+1][i] + p[i-1]*p[k]*p[j] 
                cost[i][j] = min(cost[i][j],q) 
                k +=1
            i +=1 
        Clen +=1
    return cost[1][n-1]
if __name__ == "__main__":
    arr = [1,2,5,4,6]
    n = len(arr)
    print(MatrixChainOrder(arr,n))