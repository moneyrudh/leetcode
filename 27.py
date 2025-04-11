class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x != val]; return len(nums)
        # i, j, k = 0, 0, 0
        # n = len(nums)

        # while i < n:
        #     if nums[i] != val:
        #         nums[j] = nums[i]
        #         j += 1
        #         k += 1
        #     i += 1

        # return k