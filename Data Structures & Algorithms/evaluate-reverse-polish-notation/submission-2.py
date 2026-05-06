class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)): 
            if tokens[i] in "+-*/": 
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if tokens[i] == "+": 
                    temp = num1 + num2
                elif tokens[i] == "-": 
                    temp = num1 - num2
                elif tokens[i] == "*":
                    temp = num1 * num2
                else: 
                    temp = int(num1 / num2)
                stack.append(temp)
            else: 
                stack.append(int(tokens[i]))
        return stack[-1]