class Test:
    def __init__(self):
        self.flag = None
    def getFlag(self):
        return self.flag
    def isNumber(self,c):
        return c >= "0" and c<= "9"
    def strToint(self,s1):
        if s1 == None:
            self.flag = False
            print("not a number")
            return -1
        self.flag = True
        res = 0
        i = 0
        minus =  False 
        if list(s1)[i] == "-":
            minus = True
            i +=1
        if list(s1)[i] == "+":
            i +=1
        while i < len(s1):
            if self.isNumber(list(s1)[i]):
                res = res*10  +  ord(list(s1)[i]) - ord('0')
            else:
                self.flag = False
                print("not a number")
                return False
            i+=1
        return -res if minus else res 
if __name__ == "__main__":
    s1 = "200"
    s2 = "-200"
    s3 = "+200"
    s4 = "++200"
    
    t = Test()
    print(t.strToint(s1))
    print(t.strToint(s2))
    print(t.strToint(s3))
    print(t.strToint(s4))
