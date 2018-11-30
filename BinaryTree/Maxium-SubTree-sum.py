class BitNode:
    def __init__(self,val):
        self.val = val
        self.lchild = None
        self.rchild = None
    
class Test: 
    def __init__(self):
        self.maxSumNum = -2**31


    def FindMaxNumSubTree(self,root,maxRoot):
        if root == None:
            return 0
        lmax = self.FindMaxNumSubTree(root.lchild,maxRoot) 
        rmax = self.FindMaxNumSubTree(root.rchild,maxRoot)
        #print(lmax,rmax,root.val)
        sums = lmax + rmax + root.val 
    
        if sums > self.maxSumNum: 
            self.maxSumNum = sums
            maxRoot.val = root.val
        return sums


    def constructT(self):
        root = BitNode(6)
        node1 = BitNode(3) 
        node2 = BitNode(-1)
        node3= BitNode(7)
        node4 = BitNode(9)
        node5 = BitNode(11)
        root.lchild = node1
        root.rchild = node2
        node1.lchild = node3
        node1.rchild = node4
        node2.lchild = node5
        
        node2.rchild = None
        node3.lchild = node3.rchild =None
        node4.lchild = node4.rchild =None
        node5.lchild = node5.rchild =None
        
        return root
if __name__ == "__main__":
    test = Test()
    root = test.constructT()
    #print(root.val)
    maxRoot = BitNode(-2**31)
    test.FindMaxNumSubTree(root,maxRoot) 
    print(test.maxSumNum) 
    print(maxRoot.val)