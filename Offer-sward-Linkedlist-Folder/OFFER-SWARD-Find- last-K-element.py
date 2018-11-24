class LNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def Construct():
    i = 1
    head = LNode(None)
    head.next = None

    cur = head
    tmp = None
    
    while i< 11:
        tmp = LNode(i)
        tmp.next = None
        cur.next= tmp
        cur = cur.next
        i+=1
    return head 
def PrintList(head):
    cur = head.next
    print("生成列表：",end=" ") 
    while cur != None:
        print(cur.val)
        cur =cur.next
    
def find_last_K(head, k):
    i = 0 
    if head is None or head.next is None :
        return head

    slow = head.next
    fast = head.next 

    while i< k and fast != None:
        fast =  fast.next 
        i = i+1

    #then we start another loop

    while fast != None:
        slow = slow.next
        fast = fast.next 
    
    return slow

if __name__ == "__main__":
    head = Construct() 
    result = None
    PrintList(head) 
    result =  find_last_K(head,3 )
    print(result.val)