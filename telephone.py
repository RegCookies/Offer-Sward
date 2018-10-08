import sys 

a = []
for i in sys.stdin:
    a.append(i.strip("\n"))

req_list = a[1:]

#tele_list = ["ZERO", "ONE", "TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE" ]

for s in req_list:
    n2 = s.count("Z")
    n4 = s.count("W")
    n6 = s.count("U")
    n8 = s.count("X")
    n0 = s.count("G")
    n5 = s.count("H")-n0
    n7 = s.count("F")-n6
    n3 = s.count("O")-n2-n4-n6
    n9 = s.count("V")-n7
    n1 = s.count("I")-n7-n8-n0
    print("0"*n0+"1"*n1+"2"*n2+"3"*n3+"4"*n4+"5"*n5+"6"*n6+"7"*n7+"8"*n8+"9"*n9)
    
