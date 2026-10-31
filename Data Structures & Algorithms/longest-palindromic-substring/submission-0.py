class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub=s[i:j]
                if sub==sub[::-1]:
                    if len(sub) > len(res):
                        res = sub
        return res