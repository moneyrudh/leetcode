class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted([(k, v) for k, v in Counter(nums).items()], key=lambda a: a[1], reverse=True)[0][0]