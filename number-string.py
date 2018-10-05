import sys 
a=[]
for i in sys.stdin:
    a.append(i.strip("\n"))
nums = a[1].split(" ")
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        #print(nums[i],nums[j],(nums[i] + nums[j] < nums[j] + nums[i]))
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i],nums[j]  = nums[j], nums[i]
print(''.join(nums))

