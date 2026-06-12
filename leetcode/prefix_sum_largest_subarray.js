function maxSubArrayLen(nums, target) {
  const prefixMap = { 0: -1 }; // Maps prefixSum -> earliest index
  let currentSum = 0;
  let maxLength = 0;

  for (let i = 0; i < nums.length; i++) {
    currentSum += nums[i];

    // Check if the required complement exists
    const complement = currentSum - target;
    if (complement in prefixMap) {
      maxLength = Math.max(maxLength, i - prefixMap[complement]);
    }

    // Only store the earliest index to maximize the subarray length
    if (!(currentSum in prefixMap)) {
      prefixMap[currentSum] = i;
    }
  }

  return maxLength;
}
