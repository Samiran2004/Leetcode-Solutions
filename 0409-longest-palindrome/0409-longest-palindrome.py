class Solution:
    def longestPalindrome(self, s: str) -> int:
        seen = set()
        length = 0

        for char in s:
            # If we seen this character before...
            if char in seen:
                seen.remove(char)
                length += 2
            else:
                seen.add(char)
        
        if seen:
            length += 1
        
        return length