#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List

def removeDuplicates(nums: List[int]) -> int:

    if not nums:
        return 0
    
    nums_len = len(nums) 
    k = nums_len # let's assume they're all unique
    empty_positions = [] # to hold empty positions to fill in

    if nums_len >= 1:
        last_non_repeat_number = nums[0] # set the comparison number to the first element of the array
        for i in range(1, nums_len):
            if nums[i] == last_non_repeat_number:
                nums[i] = None
                empty_positions.append(i)        
                k = k - 1                
            else:
                last_non_repeat_number = nums[i]
                if len(empty_positions) > 0:
                    nums[empty_positions.pop(0)] = last_non_repeat_number
                    nums[i] = None
                    empty_positions.append(i)
                
    return k

if __name__ == "__main__":
    
    nums = [0,0,1,1,1,2,2,3,3,4]

    k = removeDuplicates(nums)
    print(f"k = {k}\n nums:{nums}")
