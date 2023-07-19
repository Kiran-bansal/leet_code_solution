class Solution(object):
    def isPalindrome(self, s):
        import re
        new_s = re.sub(r"[^a-zA-Z0-9\\s+]", "", s).lower()
        return new_s == new_s[::-1]
