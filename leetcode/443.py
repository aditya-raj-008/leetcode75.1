class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        :type chars: List[str]
        :rtype: int
        """
        res_str=[]
        c=1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                c=c+1
                continue
            else:
                res_str.append(str(chars[i]))
                if c>1 and c<10:
                    res_str.append(str(c))
                elif c>=10:
                    k=str(c)
                    res_str.append(list(k))
                    
                c=1
        if c==1:
            res_str.append(str(chars[-1]))
        elif c>1:
            res_str.append(str(chars[-1]))
            res_str.append(str(c))
        chars=res_str
        return len(chars)

