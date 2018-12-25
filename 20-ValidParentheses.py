class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0: # len(s) must be even number
            return False
        elif len(s) == 0:
            return True
        open_brackets = ['(', '[', '{']
        closed_brackets = [')', ']', '}']
        dic = dict(zip(closed_brackets, open_brackets))
        stack = []
        for c in s:
            if c in open_brackets: # put open brackets into stack
                stack.append(c)
            else: # when meet a closed bracket
                if not stack or stack[-1] != dic[c]:
                    return False
                stack.pop()
        return len(stack) == 0