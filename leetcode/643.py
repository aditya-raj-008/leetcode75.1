class Solution:
    def findMaxAverage(self, nums,k):
        sum_1=0
        nums=tuple(nums)
        avg=sum_1/k
        max_avg=-32645986
        for i in range(len(nums)-k+1):
            sum_1=sum(nums[i:i+k])
            avg=sum_1/k
            if avg>max_avg:
                max_avg=avg
        return max_avg
