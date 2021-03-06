class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for item in path.split("/"):
            if item not in [".", "..", ""]:
                stack.append(item)
            if item == ".." and stack:
                stack.pop()
        return "/" + "/".join(stack)

    def simplifyPath_self(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        special = {'.', '..', ''}
        for item in path.split('/'):
            if item not in special:
                stack.append(item)
            elif item == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)
