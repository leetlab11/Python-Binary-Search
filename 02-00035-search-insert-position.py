# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Example 2:
# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Example 3:
# Input: nums = [1,3,5,6], target = 7
# Output: 4
 
# Constraints:
# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

# YT Video Link: https://youtu.be/K-RYzDZkzCI?si=Wjlvm3X2Bl2O4mvQ

# -------------------------------------------------------------------------------------------------------------------------------------------

# BINARY SEARCH
# implement Binary Search- this will give target value if it's present
# m = (r + l) // 2 OR (r - l) // 2 + l to calculate midpoint
# if target is found, return that (m)
# if target is not found, move l and r pointers- l = m + 1; r = m - 1
# if target is not in the array, l is always updated such that it;s at the insert position
# thsi is because either l or r will move depending on target value, and at some point l > r- this is the point where while loop will break and l will be at the insert position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] == target:
                return m
            
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
        return l

Time Complexity = O(logn)
Space Complexity = O(1)
