class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        upper=len(prices)
        output=0
        while r<upper:
            if prices[l]>prices[r]:
                l=r
                r=r+1
            else:
                diff=prices[r]-prices[l]
                print(diff)
                r=r+1
                output=max(output,diff)
        return output

            
            


        