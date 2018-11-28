class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def constructL(i): 
    head =LNode(None)
    head.next = None
    cur = head
    tmp = None 
    while i<11:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp 
        i += 2
    return head

def printL(head):
    cur = head.next
    while cur != None:
        print(cur.val,end = " ") 
        cur = cur.next


def mergeL(head1,head2):
    if head1 is None or head1.next is None:
        return head2 
    if head2 is None or head2.next is None:
        return head1
        
    cur1 = head1.next
    cur2 = head2.next
    
    head = None
    cur = None

# 确定合并后的头节点 

    if cur1.val > cur2.val:
        head = head2
        cur = cur2
        cur2 = cur2.next

    else:
        head = head1
        cur = cur1 
        cur1 = cur1.next

    while cur1 != None and cur2 != None:
        if cur1.val < cur2.val:
            cur.next = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            cur.next = cur2
            cur = cur2 
            cur2 = cur2.next

    if cur1 != None: 
        cur.next = cur1
    if cur2 != None:
        cur.next = cur2
    
    return head 

if __name__ == "__main__":
    head1 = constructL(1)
    head2 = constructL(2)
    
    printL(head1)
    printL(head2)
    
    head = mergeL(head1,head2)
    printL(head)