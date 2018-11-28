class LNode:
    def __init__(self,val):
        self.val = val 
        self.next = None

def printL(head):
    cur = head.next
    while cur != None:
        print(cur.val,end = " ") 
        cur = cur.next

def Delete_point(node):
    if node is None or node.next is None:
        return False
    node.val = node.next.val
    node.next = node.next.next
    
    return True 

if __name__ == "__main__":
    i = 1 
    head = LNode(None)
    head.next = None
    cur = head
    p = None
    
    while i< 11 :
        tmp = LNode(i) 
        tmp.next = None 
        cur.next = tmp 
        cur = tmp
        if i== 4:
            p = tmp
        i +=1

    printL(head)
    print("\n") 
    result = Delete_point(p)
    if result:
        printL(head)
    
    