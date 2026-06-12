class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s = set(candyType)
        h = int(len(candyType) // 2)

        if len(s) == h or len(s) > h:
            return h
        else:
            return len(s)