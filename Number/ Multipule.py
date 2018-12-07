def divide(m,n): 
    result = 0
    while m>=n:
        multi = 1
        while multi*n  <= (m>>1):
            multi <<= 1  
        result += multi 
        m -=  multi *n 
    
    print(result, m) 

if __name__ == "__main__":
    m = 14
    n = 4
    divide(m,n)