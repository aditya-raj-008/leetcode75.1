class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1=len(word1)
        len2=len(word2)
        if len1>len2:
            l=len2
            k=word1[len2:len1]
        else:
            l=len1
            k=word2[len1:len2]
        k1=""
        for i in range(l):
            k1=k1+word1[i]+word2[i]
        return k1+k