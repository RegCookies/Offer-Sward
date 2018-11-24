class LNode:
    def __init__(self,node):
        self.node = node
        self.val = None
        self.next = None
    
def reverse(head):
    if head is None or head.next is None:
        return 
    # Initialize Node
    pre = None
    cur = None
    next = None

    # Then initialize the position of Node
    cur = head.next
    next = cur 
    #print(cur.val, pre.val,next.val)
    while cur.next != None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
        print(cur.val, pre.val,next.val)
    
    print(cur.val,pre.val,next.val)
    head.next = cur
    cur.next = pre

# now we do the Recursice method:
def recur_reverse(head):
    if head is None or head.next is None:
        return head
    else:
        new_head = recur_reverse(head.next)
        head.next.next = head
        head.next = None 
    return new_head
    

# then test the return:
if __name__ == "__main__":
    # first of all , create the linked list
    head = LNode(None)
    i = 1 
    head.next = None 
    tmp = None
    cur = head

    while  i < 10:
        tmp = LNode(None)
        tmp.val = i
        #tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1 
    print("排序之前：")
    cur = head.next
    while cur!= None:
        print(cur.val)
        cur = cur.next
    cur = recur_reverse(head)

    #cur = head.next
    print("\n逆序后：")
    while cur != None:
        print(cur.val)
        cur = cur.next
    
    # the time cost is O(n) we only need to scan these once
