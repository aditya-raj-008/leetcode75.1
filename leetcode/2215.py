class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]):
        nums1=set(nums1)
        nums2=set(nums2)
        l1=[]
        l2=[]
        answer=[]
        for i in nums1:
            if i not in nums2:
                l1.append(i)
        for j in nums2:
            if j not in nums1:
                l2.append(j)
        answer.append(l1)
        answer.append(l2)
        return answer