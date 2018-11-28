class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def IsIntesect(head1,head2):
    if head1 is None or head1.next is None:
        return None
    if head2 is None or head2.next is None:
        return None
    if head1 == head2:
        return None
        
    tmp1 = head1.next
    tmp2 = head2.next
    
    l1=0
    l2=0
    while tmp1.next != None:
        tmp1 = tmp1.next
        l1 += 1

    while tmp2.next != None:
        tmp2 = tmp2.next 
        l2 += 1

    if tmp1 == tmp2:
        if l1 > l2:
            while l1 - l2 > 0:
                head1 = head1.next
                l1 -= 1
        if l2 > l1 : 
            while  l2 - l1 > 0:
                head2 = head2.next
                l2 -= 1 

        while head1 != head2 :
            head1 = head1.next
            head2 = head2.next
        return head1
    else:
        return None

if __name__ == "__main__":
    i = 1
    head1 = LNode(None)
    head1.next = None
    head2 = LNode(None)
    head2.next = None
    tmp = None 
    cur = head1
    p = None

    while i<8:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp
        if i== 5:
            p = tmp
        i+= 1

    cur = head2
    while i < 5:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur= tmp 
        i +=1 

    cur.next = p 
    
    interNode = IsIntesect(head1,head2)
    
    if interNode is None:
        print("不相交")
    else: 
        print("相交"+ str(interNode.val)) 


     