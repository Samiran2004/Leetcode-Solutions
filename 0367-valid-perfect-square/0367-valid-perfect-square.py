class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        # if num == 1:
        #     return True

        # for i in range(1, num):
        #     if i * i == num:
        #         return True
        #     elif i * i > num:
        #         break
        
        # return False


        left, right = 1, num

        while left <= right:
            mid = (left + right) // 2

            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        
        return False