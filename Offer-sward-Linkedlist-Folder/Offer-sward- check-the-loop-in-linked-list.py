#Initialize the node
class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None 

#then construct the list node：

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
    cur.next = head.next.next.next
    return head 

# then find whether it has a loop
def loop_or_not(head):
    if head is None or head.next is None:
        return None
    slow = head.next
    fast = head.next

    while fast != None or fast.next != None: 
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast :
            return slow 
    return None

def find_loop(head,meetNode):
    first = head.next
    second = meetNode
    
    while first != second:
        first = first.next
        second = second.next
    return first

if __name__ == "__main__":
    head = constructList()
    meetNode = loop_or_not(head)
    loopNode = None
    if meetNode != None:
        print("有环")
        loopNode = find_loop(head,meetNode)
        print("环的入口点为： "+ str(loopNode.val))
    else:
        print("没有环")
    