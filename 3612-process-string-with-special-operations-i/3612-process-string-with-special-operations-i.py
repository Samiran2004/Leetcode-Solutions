class Solution:
    def processStr(self, s: str) -> str:
        
        ans = ""

        for char in s:
            if 'a' <= char <= 'z':
                ans += char
            
            elif char == "*":
                if ans:
                    ans = ans[:-1]
            elif char == "#":
                ans += ans
            else:
                ans = ans[::-1]
        
        return ans