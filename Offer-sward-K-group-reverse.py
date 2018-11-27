class LNode:
    def __init__(self,val):
        self.val = val
        self.next = None

def reverseL(head):
    if head is None or head.next is None:
        return head
    
    pre = head
    cur = head.next
    next = cur.next
    
    pre.next = None
    
    while cur != None:
        next = cur.next 
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverseK(head,K):
    if head is None or head.next is None or K<2 :
        return 
    i = 1
    pre = head
    begin = head.next
    end = None
    next = None 
    while begin != None :
        end = begin
        while i< K:
            if end.next != None:
                end = end.next
            else:
                return

            i+= 1
        next =  end.next
        end.next = None
        pre.next = reverseL(begin)
        begin.next = next
        pre = begin 
        begin = next 
        i = 1

def constructed():
    i = 1
    head = LNode(None)
    head.next = None
    tmp = None
    cur = head
    
    while i<11:
        tmp = LNode(i)
        tmp.next = None
        cur.next = tmp
        cur = tmp
        i += 1
        
    return head

if __name__ == "__main__":
    head = constructed()
    print("顺序输出：",end = " " ) 
    cur = head.next
    while cur!= None :
        print(cur.val,end = " " )
        cur= cur.next
    reverseK(head,3)
    print("\n 分组输出",end = " " )
    cur = head.next 
    while cur!= None:
        print(cur.val,end= " ") 
        cur = cur.next 