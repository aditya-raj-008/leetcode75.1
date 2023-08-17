class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp_list=s.strip().split()
        rev_string=""
        for i in range(len(temp_list)):
            rev_string += temp_list[-i-1] +" "
        rev_string=rev_string[0:-1]
        return rev_string