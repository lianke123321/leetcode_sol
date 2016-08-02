# no Liana solution


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        post_to_pre = {i: set() for i in xrange(numCourses)}
        pre_to_post = {i: set() for i in xrange(numCourses)}

        for i, j in prerequisites:
            post_to_pre[i].add(j)
            pre_to_post[j].add(i)
        print post_to_pre, pre_to_post
        stack = [i for i in xrange(numCourses) if len(post_to_pre[i]) == 0]
        result = []
        while stack:
            node = stack.pop()
            result.append(node)
            for i in pre_to_post[node]:
                post_to_pre[i].remove(node)
                if len(post_to_pre[i]) == 0:
                    stack.append(i)
            del post_to_pre[node]
        return result if not post_to_pre else []

sol = Solution()
print sol.findOrder(3, [[1, 0], [2, 0]])
