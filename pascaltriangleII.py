class Solution(object):
    def getRow(self, rowIndex):
        b = []
        for i in range(rowIndex+1):
            k = self.solve(rowIndex,i)
            b.append(k)
        return b
            


    def solve(self,n,r): #to solve the nCr function
        ans = 1
        for i in range(r):
            ans = ans*(n-i)
            ans = ans//(i+1)
        return ans
