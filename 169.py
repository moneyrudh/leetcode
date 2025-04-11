class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return sorted([(k, v) for k, v in Counter(nums).items()], key=lambda a: a[1], reverse=True)[0][0]
        current_max = [-1, 0] # [number, frequency]
        prev_max = [-1, 0]
        t = [-1, -1]
        n = len(nums)

        i = 0
        while i < n:
            count = 0
            start = i
            num = nums[start]
            while i < n and nums[i] == nums[start]:
                i += 1
                count += 1

            if current_max == [-1, 0]:
                current_max[:] = [num, count]
            elif current_max[0] == num:
                current_max[1] += count
            elif count > current_max[1]:
                prev_max[:] = current_max[:]
                current_max[:] = [num, count]
            elif prev_max == [-1, 0] or prev_max[0] == num:
                prev_max[:] = [num, prev_max[1] + count]
                if prev_max[1] > current_max[1]:
                    t[:] = prev_max[:]
                    prev_max[:] = current_max[:]
                    current_max[:] = t[:]

        return current_max[0]