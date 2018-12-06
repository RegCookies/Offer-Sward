def process(t,n):
    if t == None or n <= 0:
        return None
    m = len(t) 
    proTime = [0]* m 
    i = 0 
    while i < n: 
        minTime = proTime[0] + t[0] 
        minIndex = 0
        j = 1
        while j < m: 
            if minTime > proTime[j] + t[j]: 
                minTime = proTime[j] + t[j]
                minIndex = j
            j +=1
        proTime[minIndex] += t[minIndex]
    return proTime
if __name__ == "__main__":
    t = [7,10]
    n = 6 
    protime = process(t,n)
    if protime == None:
        print("ERROR")
    else: 
        totalTime = protime[0]
        i = 0
        while i <len(protime):
            print("第" + str(i+1) + "台服务器有" + str(protime[i]/t[i]) + "总执行时间"+ str(protime[i])) 

            if protime[i] > totalTime: 
                totalTime = protime[i] 
            i+=1
        print(str(totalTime))
ç