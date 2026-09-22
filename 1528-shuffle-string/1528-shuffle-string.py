class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = ""
        
        for i in range(len(s)):
            res += s[indices.index(i)]
        
        return res