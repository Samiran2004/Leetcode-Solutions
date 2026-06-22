class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        charMap = {}

        for char in text:
            if char == 'b' or char == 'a' or char == 'l' or char == 'o' or char == 'n':
                charMap[char] = charMap.get(char, 0) + 1
        
        fCat = min(charMap.get('b', 0), charMap.get('a', 0), charMap.get('n', 0))
        sCat = min(charMap.get('l', 0), charMap.get('o', 0))

        return min(sCat // 2, fCat)