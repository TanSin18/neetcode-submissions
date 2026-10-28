class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique=set(nums)
        longest=0
        for num in nums:
            if (num-1) not in unique:
                length=1
                while(num+1) in unique:
                    num=num+1
                    length=length+1
                longest=max(length,longest)
        return longest
                
        