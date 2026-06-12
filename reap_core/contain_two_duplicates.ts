function contains_two_duplicates_of_k_distance(nums: Array<number>, k_distance: number): boolean {
  // store the numbers we seen and their index.
  const seen: Record<number, number> = {};

  // returns true if two numbers a and b are the same and the distance is <= k.
  for (let index = 0; index < nums.length; index++) {
    let value = nums[index];

    // if we have not seen it, add to seen map
    if (!(value in seen)) {
      seen[value] = index;
      continue;
    }

    const previous_index = seen[value];
    const distance = index - previous_index;
    if (distance <= k_distance) return true;

    // update index, so we dont measure to far a distance
    seen[value] = index;
  }

  return false;
}
