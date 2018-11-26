class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def constructList():
    i = 1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head 

    while i < 11:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = cur.next
        i += 1
    cur.next = None 
    return head 
def nearby_reverse(head):
    if head is None or head.next is None or head.next.next is None:
        return head
    pre = head
    cur = head.next
    nextN= None
    while cur!= None and cur.next!= None :
        nextN = cur.next.next 
        pre.next = cur.next
        cur.next.next = cur
        cur.next = nextN
        pre = cur
        cur = nextN 
if __name__ == "__main__":
    head = constructList()
    nearby_reverse(head)

    print(head.val,head.next.val)    
    cur = head.next
    
    while cur != None:
        print(cur.val,end = " ")
        cur = cur.next 
    