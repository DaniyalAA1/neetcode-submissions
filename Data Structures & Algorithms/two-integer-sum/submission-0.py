class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        # target - nums[i] is in there, then done
        #pseudocde it out
        # see if the target value minus the curent value is in my map
        #then i have the two values that add up to target
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in my_dict:
                return [my_dict[diff], i]
            else: 
                my_dict[nums[i]] = i
            
        