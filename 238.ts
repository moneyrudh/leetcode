function productExceptSelf(nums: number[]): number[] {
  let res: number[] = Array(nums.length).fill(1);
  for(let i=1; i<nums.length; i++) {
    res[i] = res[i-1] * nums[i-1];
  }
  for(let i=nums.length-2; i>=0; i--) {
    nums[i] *= nums[i+1];
    res[i] *= nums[i+1];
  }
  return res;
};
