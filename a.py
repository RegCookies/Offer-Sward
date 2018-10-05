A = "aba"
B = "b"

def hui(a):
    print(a,a[::-1])
    if a == a[::-1]:
        return True
    return False
count = 0
if len(A)<len(B):
    A,B = B,A
for i in range(len(A)+1):
    c = A[:i]+B+A[i:]
    print(c,hui(c))
    if hui(c):
        count+=1
print(count)
