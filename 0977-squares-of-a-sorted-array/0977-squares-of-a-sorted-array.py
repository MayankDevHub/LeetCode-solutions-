class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        squared_array = []
        decreasing_squared_array=[]
        
        for i in nums:
            squared_array.append(i*i)
        decreasing_squared_array = sorted(squared_array)

        return  decreasing_squared_array