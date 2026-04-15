from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if len(stack) <= 0:
                    return False
                first = stack.pop()
                if first == "{" and char != "}":
                    return False
                elif first == "(" and char != ")":
                    return False
                elif first == "[" and char != "]":
                    return False

        return len(stack) == 0