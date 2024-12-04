from typing import List, Optional


class Solution:
    def twoSum(self, nums: List[int], target: int) -> Optional[List[int]]:
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return None


# Test cases
def test_two_sum():
    solution = Solution()

    # Test case 1: Valid solution
    nums = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(nums, target)
    print(f"Test Case 1 - Expected: [0, 1], Got: {result}")

    # Test case 2: Another valid solution
    nums = [3, 2, 4]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Test Case 2 - Expected: [1, 2], Got: {result}")

    # Test case 3: No solution
    nums = [1, 2, 3]
    target = 7
    result = solution.twoSum(nums, target)
    print(f"Test Case 3 - Expected: None, Got: {result}")

    # Test case 4: Multiple possible pairs
    nums = [1, 3, 3, 2]
    target = 6
    result = solution.twoSum(nums, target)
    print(f"Test Case 4 - Expected: [1, 2], Got: {result}")


# Run tests
test_two_sum()
