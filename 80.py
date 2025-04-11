class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j = 0, 0
        n = len(nums)

        while j < n:
            count = 0
            start = j
            while j < n and nums[j] == nums[start]:
                j += 1
                count += 1

            count = min(count, 2)

            while count > 0:
                nums[i] = nums[j-1]
                i += 1
                count -= 1

        return i