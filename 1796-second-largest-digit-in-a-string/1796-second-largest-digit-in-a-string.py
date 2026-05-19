class Solution:
    def secondHighest(self, s: str) -> int:
        intArr = []

        for char in s:
            if char.isdigit():
                intArr.append(int(char))
        
        if len(intArr) == 0:
            return -1
            
        intArr.sort()
        maximum = intArr[-1]
        n = len(intArr)
        for i in range(n - 2, -1, -1):
            if intArr[i] != maximum:
                return intArr[i]
        
        return -1