function max_sub_array_length(nums, target) {
  seen_totals = { 0: -1 }; // store the sum and what index we saw them, we start map with sum(0) at -1 just to ensure we cover the index from when we've yet to sum anything.

  let max_length = 0;
  let last_sum = 0; // the last sum of the last index (index - 1)
  for (let index = 0; index < nums.length; index++) {
    let current_value = nums[index];
    // get the next sum
    last_sum = last_sum + current_value;

    // if we found the index where its zero again, so push
    let old_sum = last_sum - target;
    if (old_sum in seen_totals) {
      let current_length = index - seen_totals[old_sum];
      max_length = Math.max(current_length, max_length);
    }

    // its important to ensure we dont overwrite a previous sum
    // similar to this sum, because we need to know which index it first occurs
    // at, so skip if already in the map
    if (!(last_sum in seen_totals)) {
      seen_totals[next_sum] = index;
    }
  }

  return max_length;
}
