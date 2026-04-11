# 1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.


The trick here is similar to the #[./max-consecutive-ones.md] where k is set to 1 and we just count
how many 1s we can find consequentively with 1 zero allowed and then remove that zero (basically -1)
from the max_length of 1.

```bash
SubArray:  [1, 1, 1]  | max_len:  2
SubArray:  [1, 0, 0]  | max_len:  1
SubArray:  [0, 0, 1]  | max_len:  1
SubArray:  [0, 0, 0, 0]  | max_len:  0
SubArray:  [1, 1, 0, 1]  | max_len:  3
SubArray:  [0, 1, 1, 1, 0, 1, 1, 0, 1]  | max_len:  5
```
