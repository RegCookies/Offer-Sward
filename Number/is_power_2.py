def isPower(n): 
    return n&(n-1) == 0 

if __name__ == "__main__":
    n1 =3
    n2 =4

    print(isPower(n1))
    print(isPower(n2))