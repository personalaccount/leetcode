# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # if nums2 is empty - do nothing
        if n == 0:
            return

        #if nums1 is empty, fill it in with nums2 values
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
                return

        #if nums1 is not empty sort and reassign
        if (m > 0):
            for i in range (m+n):
                for j in range(n):
                    #compare the last element of nums1 to the first element of nums2 
                    # if it's smaller, then fill out the rest of the array with nums2 elements
                    if nums1[m - 1] < nums2[j]:
                        nums1[m + j] = nums2[j]
                        return
                    else:
                        cache = [m+n]
                        if nums1[]
                        





        print (nums1)

def main():

    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3

    sol = Solution()
    sol.merge(nums1, m, nums2, n)


if __name__ == "__main__":
    main()
