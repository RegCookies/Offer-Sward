class LNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def count_the_total_value(l1,l2):
    if l1 is None or l1.next is None:
        return l2
    if l2 is None or l2.next is None:
        return l1

    # then we start to add 
    
    count = 0
    sums = 0
    tmp = None
    # create the result linked List
    p1 = l1.next
    p2 = l2.next
    p = LNode(None)
    res = p

    while p1 is not None or p2 is not None :
       #print(p1.val,p2.val)
        if p1 is None:
            sums =  p2.val + count
        elif p2 is None:
            sums =  p1.val + count
        else:
            sums = p1.val + p2.val + count

        data = sums % 10
        count = sums // 10
        
        #print(res.val,sums,data,count)
        tmp = LNode(data) 
        tmp.next = None 
        res.next = tmp
        res = res.next
        print(res.val)
        if p1 is None: 
            p2 = p2.next 
        elif p2 is None:
            p1 = p1.next
        else:
            p1 = p1.next
            p2 = p2.next
    
    if count == 1:
        tmp = LNode(count)
        tmp.next = None
        res.next = tmp
        res = res.next
    return p 

if __name__ == "__main__": 
    i = 0
    l1 = LNode(None)
    l2 = LNode(None)
    
    tmp = None
    
    cur = l1
    res = None
     
    print("构造第一个：") 
    
    while  i<7 : 
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp 
        cur = cur.next
        i +=1

    cur = l2

    print("构造第二个:")
    i = 0
    while i<11:
        tmp = LNode(i+2)
        tmp.next =None
        cur.next = tmp
        cur = cur.next
        i +=1

    # do the cal

    cur = l1.next
    print("构造表一:",end =" ")
    
    while cur != None:
        print(cur.val,end = " ")
        cur = cur.next

    cur = l2.next

    print("\n构造表二：",end= " ")
    while cur !=  None :
        print(cur.val,end =" ") 
        cur = cur.next 
    
    res =  count_the_total_value(l1,l2)

    print("\n结果列表：",end = " ")
    
    cur = res.next 
    while cur != None: 
        print(cur.val,end= " ") 
        cur = cur.next

    