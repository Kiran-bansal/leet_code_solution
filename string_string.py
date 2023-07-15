class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        if n < m:
            return -1
        for i in range(n - m + 1):
            if haystack[i:i + m] == needle:
                return i
        return -1
