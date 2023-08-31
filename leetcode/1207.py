class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d={}
        for i in arr:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        list_val=list(d.values())
        set_list=set(list_val)
        if len(list_val)==len(set_list):
            return True
        else:
            return False