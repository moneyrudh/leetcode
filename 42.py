class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        right_max = [0] * n

        cur_max = 0
        for i in range(n-1, -1, -1):
            right_max[i] = cur_max
            cur_max = max(cur_max, height[i])

        left_max = 0
        for i in range(n):
            left_max = max(left_max, height[i])
            left = left_max
            right = right_max[i]
            h = height[i]

            if left <= h or right <= h:
                continue

            total += min(left, right) - h
        return total