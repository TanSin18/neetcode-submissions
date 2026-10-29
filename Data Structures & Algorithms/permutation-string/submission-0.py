class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len=len(s1)
        s2len=len(s2)
        sorted_s1 = sorted(s1)
        for i in range(s1len, s2len + 1):
            r = i - s1len
            if sorted_s1 == sorted(s2[r:i]):
                return True
        return False