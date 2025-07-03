from typing import List, Optional

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

"""


class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

if __name__ == "__main__":
    
    nums = [2,2,1,1,1,2,2]

    sol = Solution()

    k = sol.majorityElement(nums)

    print(f"The majority element is = {k}\n")
