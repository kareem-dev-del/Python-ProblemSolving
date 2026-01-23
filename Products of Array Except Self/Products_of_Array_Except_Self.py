# This function returns a list where each element is the product of all other elements except itself.
# It uses nested loops to multiply all numbers while skipping the current index.
#Day=>Four=>https://neetcode.io/

class Solution:
    def productExceptSelf(self, nums):
        result= []
        for i in range(len(nums)):
            x=1
            for j in range(len(nums)):
                if nums[i] == nums[j]:
                    continue
                else:
                    x*=nums[j]    
            result.append(x)  
        return result 
sol= Solution()
print(sol.productExceptSelf([1,2,4,6]))           