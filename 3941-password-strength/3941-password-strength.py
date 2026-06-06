class Solution:
    def passwordStrength(self, password: str) -> int:
        freq = dict()
        size = len(password)
        
        for i in range(size):
            freq[password[i]] = freq.get(password[i], 0) + 1
        
        ans = 0

        for key, value in freq.items():
            currChar = key
            if currChar >= 'a' and currChar <= 'z':
                ans += 1
            elif currChar >= 'A'and currChar <= 'Z':
                ans += 2
            elif currChar >= '0' and currChar <= '9':
                ans += 3
            else:
                ans += 5
        
        return ans