class Solution:
    def compress(self, chars: list[str]) -> int:
        """
        :type chars: List[str]
        :rtype: int
        """
        res_str=[]
        length_chars=len(chars)
        c=1
        k=0
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                c=c+1
                continue
            else:
                #chars.insert(k,str(chars[i]))
                chars[k]=str(chars[i])
                k=k+1
                if c>1 and c<10:
                    #chars.insert(k,str(c))
                    chars[k]=str(c)
                    k=k+1
                elif c>=10:
                    st=str(c)
                    stl=list(st)
                    for j in range(len(stl)):
                        #chars.insert(k,stl[j])
                        chars[k]=str(stl[j])
                        k=k+1
                    
                c=1
        if c==1 and length_chars>=1:
            #chars.insert(k,str(chars[-1]))
            chars[k]=chars[-1]
            k=k+1
        elif c>1:
            chars.insert(k,str(chars[-1]))
            k=k+1
            st=str(c)
            stl=list(st)
            for j in range(len(stl)):
                #chars.insert(k,stl[j])
                chars[k]=str(stl[j])
                k=k+1
        chars=chars[:k]
        return len(chars)