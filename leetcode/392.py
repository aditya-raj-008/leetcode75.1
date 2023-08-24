class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        flag=True
        while i<len(t) and j<len(s):
            if t[i]==s[j]:
                i=i+1
                j=j+1
            else:
                i=i+1
        if j<len(s):
            return False
        else:
            return True
