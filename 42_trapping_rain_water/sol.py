# no Liana solution


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, maxl, maxr = 0, len(height) - 1, 0, 0
        result = 0
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= maxl: maxl = height[l]
                else: result += (maxl - height[l])
                l += 1
            else:
                if height[r] >= maxr: maxr = height[r]
                else: result += (maxr - height[r])
                r -= 1
        return result

sol = Solution()
print sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
