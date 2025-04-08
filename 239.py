class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        first_max = -float("inf")
        second_max = -float("inf")
        i = 0
        n = len(nums)

        heap = [] # min heap
        maximum = []

        while i < n:
            heapq.heappush(heap, (-nums[i], i))

            if i >= k - 1:
                while heap and heap[0][1] <= i - k:
                    heapq.heappop(heap)
                maximum.append(-heap[0][0])
            i += 1

        return maximum  