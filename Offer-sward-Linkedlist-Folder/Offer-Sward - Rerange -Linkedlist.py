class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None
    
def cut(head):
    #first of all, Let's find the middle node
    if head is None or head.next is None:
        return head
    slow = head
    fast = head 
    slowpre = head #Use slow pre to cut 1inked list
    
    while fast is not None and fast.next is not None:
        slowpre = slow
        slow = slow.next
        fast = fast.next.next 
    slowpre.next = None
    return slow

#reverse the second linked list
def reverse(head):
    if head is None or head.next is None:
        return head
    
    pre = None 
    cur = None
    next = None
    
    cur = head.next
    next = cur
    
    while cur.next  != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next 
    head.next = cur 
    cur.next = pre 
    print(head.val,cur.val)
    return cur

def Recorder(head):
    if head is None or head.next is None:
        return head

    cur1 = head.next
    mid = cut(head.next) 
    # print(mid.val)
    head2 = LNode(None)
    head2.next = mid 
    cur2 = reverse(head2)
    
    tmp = None
    print(cur1.val)
    print(cur2.val)
    # now let's merge two linkedlist: 
    #while cur1.next is not None:
    #    tmp = cur1.next
    #    cur1.next = cur2
    #    cur1 = tmp
    #    tmp = cur2.next
    #    cur2.next = cur1
    #    cur2= tmp

    #cur1.next = cur2 
    #cut the linked list
    
    while cur1.next is not None:
        
        tmp = cur1.next
        cur1.next = cur2
        cur1 = tmp 

        tmp = cur2.next
        cur2.next = cur1
        cur2 = tmp
    cur1.next = cur2
    #print(cur2.val,cur2.next.val)
#Then test what you have:

if __name__ == "__main__": 
    i=1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head

    while i<8:
        tmp = LNode(i) 
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
    
    cur = head.next 
    while cur!= None:
        print(cur.val,end= " ")
        cur = cur.next

    Recorder(head)
    cur = head.next 
    print("\n")

    while cur != None:
        print(cur.val,end = " ")
        cur = cur.next
    
