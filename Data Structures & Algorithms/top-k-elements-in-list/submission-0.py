class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter={}
        for i in range(len(nums)):
            counter[nums[i]]=1+counter.get(nums[i],0)
        heap=[]
        for num in counter.keys():
            heapq.heappush(heap, (counter[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        
        

        