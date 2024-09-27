import operator


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }
        stack = []

        for token in tokens:
            if token in ops.keys():
                op1, op2 = int(stack.pop()), int(stack.pop())
                stack.append(ops[token](op2, op1))
            else:
                stack.append(token)

        return int(stack[0])
