import sys
a = []
for i in sys.stdin:
     a.append(i.strip("\n").split(" "))




for i in a:
    result = []
    for j in range(int(i[0]), int(i[1])+1):
        
        if  (j%10)**3 + (j//100)**3 + ((j//10)%10)**3 == j :

            result.append(str(j))

    if result == []:
        print("no")
    else:
        print(" ".join(result))
