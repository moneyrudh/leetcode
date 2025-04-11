class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)
        while j < n:
            start = j
            while j < n and nums[j] == nums[start]:
                j += 1
            nums[i] = nums[j-1]
            i += 1

        return i