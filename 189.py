class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not k:
            return

        n = len(nums)

        def lcm(x: int, y: int) -> int:
            i, j = x, y
            while x != y:
                if x < y:
                    x += i
                elif x > y:
                    y += j
            return x

        def gcd(x: int, y: int) -> int:
            return (x * y) // lcm(x, y)

        def helper(index: int) -> int:
            i, j = index, (index + k) % n
            t = nums[i]
            while j != i:
                cur = nums[j]
                nums[j] = t
                t = cur
                j = (j+k) % n
            return t

        for i in range(gcd(n, k)):
            nums[i] = helper(i % n)