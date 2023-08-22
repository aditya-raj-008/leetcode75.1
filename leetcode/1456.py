class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=("a","e","i","o","u")
        str_len=len(s)

        max_count=0
        for i in range(k):
            if s[i] in vowels:
                max_count=max_count+1
        if str_len>k:
            i=1
            j=k
            count=max_count
            temp=count
            while j<str_len:
                if s[i-1] in vowels and s[j] not in vowels:
                    temp=count-1
                    count=temp
                    if temp>max_count:
                        max_count=temp
                elif s[i-1] not in vowels and s[j] in vowels:
                    temp=count+1
                    count=temp
                    if temp>max_count:
                        max_count=temp
                else:
                    temp=count
                    count=temp
                    if temp>max_count:
                        max_count=temp
                i=i+1
                j=j+1
            return max_count
        else:
            return max_count