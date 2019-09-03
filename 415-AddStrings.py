class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        return str(self.strToInt(num1) + self.strToInt(num2))
        
    def strToInt(self, numStr):
        exponent = len(numStr) - 1
        num = 0
        for char in numStr:
            num += int(char) * (10 ** exponent)
            exponent -= 1
        return num