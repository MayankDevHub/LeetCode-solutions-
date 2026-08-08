# from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        result = sorted(set(nums), reverse=True)

        if len(result) < 3:
            return result[0]

        return result[2]