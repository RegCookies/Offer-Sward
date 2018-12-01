class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None
        
class Test:
    def __init__(self):
        self.pStart = None
        self.pEnd =None

    def arrayToTree(self,arr,start,end):
        root =None
        if end >= start:
            mid = (end+ start)//2
            root = BitNode(arr[mid])
            root.lchild = self.arrayToTree(arr,start,mid-1)
            root.rchild = self.arrayToTree(arr,mid+1,end)
        else:
            root = None
        return root 

    def  InOrderBST(self,root):
        if root is None :
            return
        self.InOrderBST(root.lchild) 
        root.lchild = self.pEnd
        if None == self.pEnd:
            self.pStart = root
        else:
            self.pEnd.rchild = root
        self.pEnd = root
        self.InOrderBST(root.rchild)
        
