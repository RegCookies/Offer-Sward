def Fibonacci(self, n):
    # write code here
    a = [0,1,1]
    if n<3:
        return a[n]
    for i in range(3,n+1):
        a.append(a[i-1]+a[i-2])
    return a[n]
