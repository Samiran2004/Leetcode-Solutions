class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0 or s == "":
            return 0
        count = 0
        arr = s.split(" ")
        for elm in arr:
            if elm == "":
                continue
            count += 1
        return count