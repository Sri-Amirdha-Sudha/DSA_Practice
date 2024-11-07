# Contains Duplicate : Check if a value appears atleast twice
"""
Example 1:
Input: nums = [1, 2, 3, 1]
Output: true.
Explanation: 1 appeared two times in the input array.

Example 2: 
Input: nums = [1, 2, 3, 4]
Output: false
Explanation: input array does not contain any duplicate number.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        length1 = len(nums) # taking the length of entire array
        length2 = len(set(nums)) # Set gives unique value, after that seeing the length
        result = True if length1 > length2 else False
        return result


