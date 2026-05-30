class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key= lambda a: (abs(a - x), a))

        res = []
        count = 0

        for num in arr:
            res.append(num)
            count += 1

            if count == k:
                break
        
        res.sort()
        return res