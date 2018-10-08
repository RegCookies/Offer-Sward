import sys
a = []
for i in sys.stdin:
    a.append(i.strip("\n"))

line_num = a[0]
req_list = a[1:]
#print(line_num,req_list)

def lexi(a):
    dict_order = sorted(a)
    if a == dict_order:
        return True
    return False 

def len_r(a):
    for i in range(len(a)-1):
        if len(a[i]) > len(a[i+1]):
            return False 
        else:
            continue
    return True

Flag_a = len_r(req_list)
Flag_l = lexi(req_list)

if Flag_a and Flag_l:
    print("both")
elif Flag_l:
    print("lexicographically")
elif Flag_a:
    print("lengths")
else:
    print("none")

