from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(s1, s2):
            if s1+s2 > s2+s1:
                return -1
            else:
                return 1
        
        numbers = [str(elm) for elm in nums]

        numbers.sort(key=cmp_to_key(compare))

        if numbers[0] == "0":
            return "0"
        
        return "".join(numbers)