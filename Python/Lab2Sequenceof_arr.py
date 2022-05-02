def array_Check(nums):
    
    for i in range(0,len(nums)-1):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
             
                      return True
    
    return False
#nums=[1,1,2,1,2,3,]
#nums=[1, 1, 2, 3, 1]
nums=[1,1,2,4,1]

print(array_Check(nums))


# def list123(nums):
#     num =""
#     for i in nums:
#         num +=str(i)
#     if "123" in num:
#         return True
#     else:
#         return False
# nums=[1,2,3,4,5]
# print(list123(nums))
                      
