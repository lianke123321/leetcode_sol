# no Liana solution


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res, lvl, stack = 0, 0, []
        for file_or_dir_with_lvl in input.splitlines():
            file_or_dir = file_or_dir_with_lvl.strip('\t')
            curr_lvl = len(file_or_dir_with_lvl) - len(file_or_dir)

            while curr_lvl <= lvl and stack:
                stack.pop()
                lvl -= 1

            stack.append(file_or_dir)
            lvl = curr_lvl
            if '.' in file_or_dir:
                res = max(res, len('/'.join(stack)))
        return res

sol = Solution()
print sol.lengthLongestPath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
