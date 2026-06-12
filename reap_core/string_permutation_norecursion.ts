function string_permutation_iterative(text: string) {
  // 1. Sort the characters to start with the first permutation
  const chars = text.split("").sort();

  // Print the initial sorted permutation
  console.log(chars.join(""));

  while (true) {
    let i = chars.length - 2;

    // 2. Find the rightmost character that is smaller than its successor
    while (i >= 0 && chars[i] >= chars[i + 1]) {
      i--;
    }

    // If no such character is found, we have reached the last permutation
    if (i < 0) break;

    let j = chars.length - 1;

    // 3. Find the rightmost character that is larger than chars[i]
    while (chars[j] <= chars[i]) {
      j--;
    }

    // 4. Swap characters at i and j
    swap(chars, i, j);

    // 5. Reverse the sequence from i + 1 to the end
    reverse(chars, i + 1, chars.length - 1);

    // Print the next unique permutation
    console.log(chars.join(""));
  }
}

function swap(arr: string[], i: number, j: number) {
  const temp = arr[i];
  arr[i] = arr[j];
  arr[j] = temp;
}

function reverse(arr: string[], start: number, end: number) {
  while (start < end) {
    swap(arr, start, end);
    start++;
    end--;
  }
}

// Test the function
string_permutation_iterative("abc");
