class Solution:
    def search(self, nums: List[int], target: int) -> int:
        r=len(nums)
        l=0

        res=-1
        while r>l:
            mid=int((r+l)/2)
            if nums[mid]==target:
                res=mid
                return res
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid
        return res
        