class Solution:
    def singleNumber(self, arr: List[int]) -> int:

        if len(arr)==1:
            return arr[0]

        freq = {} 

        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for key,value in freq.items():
            if value == 1:
                return key



        
        
        