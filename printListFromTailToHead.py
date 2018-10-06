def printListFromTailToHead(self, listNode):
        # write code here
    result=[]
    head = listNode
    while head:
        result.append(head.val)
        head = head.next
    return result[::-1] if result != [] else []
