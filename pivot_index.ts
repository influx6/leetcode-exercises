// function pivot_index(nums: Array<number>): number {
//   // always provide an initial value else a crash will occur for empty []
//   const sum = nums.reduce((current, last) => current + last, 0);
//   console.log("Total_sum: ", sum);

//   let left_sum = 0;
//   for (let index = 0; index < nums.length; index++) {
//     let value_at_index = nums[index];

//     let right_sum = sum - left_sum - value_at_index;
//     if (right_sum === left_sum) {
//       console.log("Pivot index for:  ", nums, " index: ", index, " sum: ", right_sum, left_sum, nums[index]);
//       return index;
//     }

//     left_sum += value_at_index;
//   }

//   console.log("No index found:  ", nums);
//   return -1;
// }

// console.log(pivot_index([1, 7, 3, 6, 5, 6]));

function pivotIndex(nums: Array<number>): number {
  // always provide an initial value else a crash will occur for empty []
  const sum = nums.reduce((current, last) => current + last, 0);

  let left_sum = 0;
  for (let index = 0; index < nums.length; index++) {
    const right_sum = sum - left_sum - nums[index];
    if (right_sum === left_sum) {
      return index;
    }

    left_sum += nums[index];
  }

  return -1;
}
