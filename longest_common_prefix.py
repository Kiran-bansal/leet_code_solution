class Solution:
    def longestCommonPrefix(self,strs):
        if len(strs)==0:
            return " "
        base=strs[0]
        for i in range(len(base)):
            for word in strs[1:]:
                if len(word)==0 or word[i]!=base[i]:
                    return base[0:i]
        return base
