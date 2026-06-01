class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(arr, mid, k):
            totalHr = 0
            for i in range(len(arr)):
                totalHr += (arr[i] + mid - 1) // mid
            return totalHr <= k
        
        lo = 1
        hi = max(piles)
        res = hi

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if check(piles, mid, h) == True:
                res = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return res