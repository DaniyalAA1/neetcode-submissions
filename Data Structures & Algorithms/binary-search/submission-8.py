class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1 # + 1 because mid has already been inspected
            elif nums[mid] > target:
                right = mid - 1 # - 1 because mid has alread been inspected
        return -1
