def minNumberInRotateArray(self, rotateArray):
    # write code here
    result = []
    for i in range(len(rotateArray)-1):
        if rotateArray[i] > rotateArray[i+1]:
            return rotateArray[i+1]
