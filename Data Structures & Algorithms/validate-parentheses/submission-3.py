class Solution:
    def isValid(self, s: str) -> bool:
        if s == "" or len(s) == 1:
            return False

        open_parentheses = "[{("
        stack = list()

        for char in s:
            if char in open_parentheses:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0






        