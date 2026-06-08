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