class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        res_str=""
        len_wd1=len(str1)
        len_wd2=len(str2)
        if len_wd1<=len_wd2:
            s_word=str1
            l_word=str2
        else:
            s_word=str2
            l_word=str1
        sub_str=""
        len_s_word=len(s_word)

        if l_word[0:len_s_word]==s_word and l_word[-len_s_word:]==s_word and (len(l_word)==2*len_s_word):
            return s_word
        #if len(l_word)<=2*len_s_word:
        else:
            for i in range(len(s_word)):
                if s_word[0:i+1]==s_word[-i-1:]:
                    sub_str=s_word[0:i+1]
                    k=len(sub_str)
                    if l_word[0:k]==sub_str and l_word[-k:]==sub_str:
                        return sub_str
                    else:
                        sub_str=""
            return sub_str

        

