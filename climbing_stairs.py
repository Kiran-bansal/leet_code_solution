class Solution(object):
    def climbStairs(self, n):
        k1=0
        k2=1
        while n>0:
            k1,k2=k2,k1+k2
            n-=1

        return k2
