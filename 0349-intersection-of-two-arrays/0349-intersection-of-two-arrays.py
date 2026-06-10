import numpy as np

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = np.array(nums1)
        nums2 = np.array(nums2)
        result = np.intersect1d(nums1, nums2)
        return result.tolist()