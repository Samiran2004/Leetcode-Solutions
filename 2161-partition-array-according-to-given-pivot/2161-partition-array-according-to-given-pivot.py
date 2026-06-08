class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = []

        # For less than pivot elements...
        for num in nums:
            if num < pivot:
                ans.append(num)
        
        # For equal elements...
        for num in nums:
            if num == pivot:
                ans.append(num)
        
        # For greater than pivot elements...
        for num in nums:
            if num > pivot:
                ans.append(num)
        
        return ans


        # # Another Approach...
        # lCount = 0
        # pCount = 0
        # for num in nums:
        #     if num < pivot:
        #         lCount += 1
        #     elif num == pivot:
        #         pCount += 1
        
        # i = 0
        # j = lCount
        # k = lCount + pCount
        # res = [0] * len(nums)

        # for num in nums:
        #     if num < pivot:
        #         res[i] = num
        #         i += 1
        #     elif num == pivot:
        #         res[j] = num
        #         j += 1
        #     elif num > pivot:
        #         res[k] = num
        #         k += 1
        # return res