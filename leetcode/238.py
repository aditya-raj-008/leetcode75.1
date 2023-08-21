class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res=[1]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    res[j]=nums[i]*res[j]
        return res