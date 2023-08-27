class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        total_left=0
        total_right=total-nums[0]
        if len(nums)==1: return 0
        for i in range(0,len(nums)-1):
            if total_left==total_right:
                return i
            else:
                total_left=total_left+nums[i]
                total_right=total_right-nums[i+1]
                if i+1==len(nums)-1:
                    if total-nums[i+1]==0:
                        return i+1   
        return -1
        