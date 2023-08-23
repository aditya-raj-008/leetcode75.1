class Solution:
    def maxOperations(self, nums,k):
        len_nums=len(nums)
        count=0
        i=0
        j=i+1
        while i<len(nums)-1:
            if nums[i]<=k:
                j=i+1
                while j<len(nums):
                    if nums[i]+nums[j]==k:
                        count=count+1
                        x=nums.pop(j)
                        nums.remove(nums[i])
                        i=i-1
                        break
                    else:
                        j=j+1
                i=i+1
            else:
                i=i+1
        return count


