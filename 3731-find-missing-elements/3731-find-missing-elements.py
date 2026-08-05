class Solution:
    def findMissingElements(self, arr: List[int]) -> List[int]:
        
        large=max(arr)
        small=min(arr)
        crr=[]

        for i in range(small,large):
            if i not in arr:
                crr.append(i)
        return crr