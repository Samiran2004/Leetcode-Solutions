class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        doubleStr = (s + s)[1:-1]

        return s in doubleStr
