#完成自己建立的栈,栈操作包含:压栈，弹栈，取栈顶元素，判断栈是否为空
#获取栈元素个数
class Mystack:
    def __init__(self,item=[]):
        self.item = item 
    
    def push(self,element):
        self.item.append(element)
    
    def pop(self):
        if len(self.item) > 0:
            return self.item.pop() 

        else:
            print("栈中元素为空")
            return None   

    def isEmpty(self):
        return len(self.item) == 0
    def getTop(self): 
        if self.isEmpty():
            return  None
        else:
            return self.item[-1]

    def getElemNumber(self):
        return len(self.item)
        

if __name__ == "__main__":
    s = Mystack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7) 
     
    print("栈顶元素为："+ str(s.getTop())) 
    
    s.pop()
    print("栈顶元素为：" + str(s.getTop()))
    s.pop()
    print("是否为空栈:" + str(s.isEmpty()))
    s.pop() 
    print("栈的长度为： " + str(s.getElemNumber()))
    s.pop()
    print("是否为空栈:" + str(s.isEmpty()))
        