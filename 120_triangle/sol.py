class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        minlen = triangle[n - 1]
        layer = n - 2
        while layer >= 0: # for each layer
            for i in range(layer + 1): #check its every node
                # find the lesser of its two childer, and sum the current value in the triangle with it
                minlen[i] = min(minlen[i], minlen[i + 1]) + triangle[layer][i]
            layer -= 1
        return minlen[0]

    def minimumTotal_self(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[-1]
        layer = n - 2
        while layer >= 0:
            # be aware, here we are going through each node at the same layer
            # not different layers, the reason why we use layer is because the
            # length of one layer is related to which layer it is
            # e.g. 5th layer (triangle[4]) has 5 nodes
            for i in xrange(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
            layer -= 1
        return dp[0]

sol = Solution()
triangle = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
print sol.minimumTotal_self(triangle)
