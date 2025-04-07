class Solution:
    def three_passes(self, heights: List[int]) -> int:
        stack = [] # index
        n = len(heights)
        maximum = 0
        
        left, right = [-1] * n, [n] * n

        for i in range(n):
            height = heights[i]
            while stack and height <= heights[stack[-1]]:
                stack.pop()

            if stack:
                left[i] = stack[-1]
            stack.append(i)

        stack.clear()
        for i in range(n-1, -1, -1):
            height = heights[i]
            while stack and height <= heights[stack[-1]]:
                stack.pop()

            if stack:
                right[i] = stack[-1]
            stack.append(i)

        for i, height in enumerate(heights):
            left_i = left[i] + 1
            right_i = right[i] - 1

            maximum = max(maximum, height * (right_i - left_i + 1))

        return maximum

    def one_pass(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        n = len(heights)
        maximum = 0

        for i in range(n+1):
            left = i
            while stack and ((i == n) or stack[-1][0] >= heights[i]):
                h, index = stack.pop()
                maximum = max(maximum, h * (i - index))
                left = index
            if i < n:
                stack.append((heights[i], left))

        return maximum

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.one_pass(heights)