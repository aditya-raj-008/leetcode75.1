class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        cur=0
        m=0
        for i in range(len(gain)):
            cur=cur+gain[i]
            if cur>m:
                m=cur
        if m>0:
            return m
        else:
            return 0
