class Solution(object):
    def plusOne(self, digits):
        for i in reversed(range(len(digits))):
            if digits[i] + 1 != 10:
                digits[i] += 1
                return digits

            digits[i] = 0

            # last elem
            if i == 0:
                return [1] + digits
