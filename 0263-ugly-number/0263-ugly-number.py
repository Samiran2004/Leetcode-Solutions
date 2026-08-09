class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        # for fact in [2, 3, 5]:
        #     while n % fact == 0:
        #         n //= fact
        
        # return n == 1

        while n % 2 == 0:
            n = n // 2
        while n % 3 == 0:
            n = n // 3
        while n % 5 == 0:
            n = n // 5
        
        return n == 1