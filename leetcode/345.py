class Solution:
    def reverseVowels(self, s: str) -> str:
        list1=list(s)
        v=["A","a","e","i","o","u","E","I","O","U"]
        v1=[]
        for i in range(len(s)):
            if list1[i] in v:
                v1.append(list1[i])
        v1=v1[::-1]
        if v1:
            count1=0
            for i in range(len(s)):
                if list1[i] in v:
                    list1[i]=v1[count1]
                    count1 +=1
        return "".join(list1)