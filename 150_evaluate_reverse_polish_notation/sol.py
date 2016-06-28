class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        length = len(tokens)
        if length == 1:
            return int(tokens[0])
        for i in range(length):
            if tokens[i] == '+':
                result = int(stack[- 2]) + int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '-':
                result = int(stack[- 2]) - int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '*':
                result = int(stack[- 2]) * int(stack[- 1])
                stack.pop()
                stack.pop()
                stack.append(result)
            elif tokens[i] == '/':
                result = int(float(stack[- 2]) / int(stack[- 1]))
                stack.pop()
                stack.pop()
                stack.append(result)
            else:
                stack.append(tokens[i])
        return result

    def evalRPN_self(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for item in tokens:
            if item == '+':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 + num2)
            elif item == '-':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 - num2)
            elif item == '*':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(num1 * num2)
            elif item == '/':
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(float(num1) / num2))
            else:
                stack.append(int(item))

        return stack.pop()

sol = Solution()
test = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print sol.evalRPN_self(test)
