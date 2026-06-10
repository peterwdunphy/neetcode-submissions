class Solution:
    def isValid(self, s: str) -> bool:
        # define closing brackets
        bracket_map={')':'(', 
                     '}':'{',
                     ']':'['}
        stack = []
        # iterate over characters
        for char in s:
        # check if closing bracket
            if char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        return not stack

