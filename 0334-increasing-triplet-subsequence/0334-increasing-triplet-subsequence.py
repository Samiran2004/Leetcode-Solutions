class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        n = len(arr)

        smaller = [-1] * n
        min = 0

        for i in range(1, n):
            if arr[i] <= arr[min]:
                min = i
            else:
                smaller[i] = min
        
        greater = [-1] * n
        max = n - 1
        for i in range(n - 2, -1, -1):
            if arr[i] >= arr[max]:
                max = i
            else:
                greater[i] = max
        
        for i in range(n):
            if smaller[i] != -1 and greater[i] != -1:
                return True
        return False