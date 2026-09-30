class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        for token in tokens:
            if token in operators:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if token == '+':
                    result = operand_1 + operand_2
                elif token == "-":
                    result = operand_2 - operand_1
                elif token == "*":
                    result = operand_1*operand_2
                else:
                    result = (operand_2/operand_1)
                stack.append(int(result))
            else:
                stack.append(int(token))
        return stack.pop()
