class BitNode:
    def __init__(self):
        self.val = None
        self.lchild = None
        self.rchild = None

def ArrayToTree(arr,start,end):
    root = None
    if end >= start:
        root  = BitNode()
        mid = ((start+end+1)//2)
        root.val = arr[mid]
        root.lchild = ArrayToTree(arr,start,mid-1)
        root.rchild = ArrayToTree(arr,mid+1,end)
    else:
        root = None
    return root

def printTree(root):
    if root == None:
        return None
    if root.lchild != None:
        root.lchild = printTree(root.lchild)
    print(root.val,end= " ")
    if root.rchild != None:
        root.rchild = printTree(root.rchild)
    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8,9,10]
    
    print(arr) 
    
    root = ArrayToTree(arr,0,len(arr)-1)
    
    printTree(root)