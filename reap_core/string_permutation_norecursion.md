Yes, you can print all string permutations without recursion by using an iterative approach.
The most efficient way to do this without recursion is Heap's Algorithm or by generating the next lexicographical permutation (like C++'s std::next_permutation). This eliminates the call stack overhead and avoids creating new filtered arrays on every step.
Here is how to implement the iterative lexicographical method in TypeScript/JavaScript:
## Iterative Permutation Code

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

## Why This is Better Than Your Recursive Version

* No Call Stack Overhead: It runs entirely inside a single while loop, eliminating the risk of a Maximum call stack size exceeded error on long strings.
* In-Place Mutations: It reuses the same chars array using swap and reverse helpers instead of calling .filter() to generate new arrays on every loop.
* Handles Duplicates Naturally: If you pass a string with repeating characters (like "remember"), this algorithm automatically skips duplicate permutations, whereas your original recursive code would print identical duplicates multiple times.

Would you like to see how to optimize this further using Heap's Algorithm for faster non-lexicographical generation, or would you like to analyze the exact memory savings for longer strings?

## Explaination
## Why chars.length - 2?
To find the next permutation, we must find the pivot—the point where the string stops increasing from right to left. [1] 
Because we compare each character to its right-hand neighbor (chars[i] >= chars[i + 1]), the last character (chars.length - 1) has no neighbor to its right. Therefore, the rightmost possible index we can start checking from is the second-to-last character, which is exactly chars.length - 2. [2] 
------------------------------
## Line-by-Line Code Explanation
Let's break down the logic using "abc" as the input string.
## 1. Setup and the First Permutation

const chars = text.split("").sort();
console.log(chars.join(""));


* Line 1: Splits the string into an array (['a', 'b', 'c']) and sorts it alphabetically. Sorting ensures we start at the absolute lexicographical beginning.
* Line 2: Joins and prints this starting permutation ("abc"). [3, 4, 5] 

------------------------------
## 2. The Main Loop & Finding the Pivot

while (true) {
  let i = chars.length - 2;
  
  while (i >= 0 && chars[i] >= chars[i + 1]) {
    i--;
  }


* while (true): Loops continuously until we manually break out.
* let i = chars.length - 2;: Sets our pointer to the second-to-last index. For ['a', 'b', 'c'], index i starts at 1 (character 'b'). [6, 7] 
* The inner while loop: Scans the array from right to left. It looks for the first character that is smaller than the one immediately to its right (chars[i] < chars[i + 1]).
* Example: Comparing 'b' and 'c'. Since 'b' < 'c', the loop stops immediately. Index i stays at 1. This is our pivot point. [8, 9] 

------------------------------
## 3. Checking for the End Condition

  if (i < 0) break;


* If the inner loop decrements i all the way past 0 (making i = -1), it means every character was greater than or equal to its neighbor. The array is entirely in reverse-alphabetical order (e.g., ['c', 'b', 'a']). We have found the final permutation, so we break the loop. [10] 

------------------------------
## 4. Finding the Element to Swap With

  let j = chars.length - 1;
  
  while (chars[j] <= chars[i]) {
    j--;
  }


* let j = chars.length - 1;: Starts a second pointer at the absolute end of the array (index 2, character 'c'). [11] 
* The while loop: Scans from right to left to find the first character that is strictly greater than our pivot character chars[i].
* Example: Our pivot is chars[1] ('b'). We check chars[2] ('c'). Since 'c' > 'b', the loop stops. Index j stays at 2. [12] 

------------------------------
## 5. Swapping the Characters

  swap(chars, i, j);


* We swap the characters at indices i and j.
* Example: Swapping 'b' (index 1) and 'c' (index 2). The array changes from ['a', 'b', 'c'] to ['a', 'c', 'b']. [13, 14, 15] 

------------------------------
## 6. Reversing the Remainder

  reverse(chars, i + 1, chars.length - 1);
  console.log(chars.join(""));
}


* reverse(...): Reverses all characters to the right of our pivot index i. This resets that trailing sub-section back into its lowest possible alphabetical order, keeping our progression as small and sequential as possible.
* Example: In this first step, i + 1 is index 2, and the end is index 2. Reversing a single element does nothing. The array remains ['a', 'c', 'b'].
* console.log(...): Prints the newly generated permutation ("acb"), and the main while loop restarts to find the next one!

If you want to track how this handles duplicate letters, would you like to trace through what happens step-by-step with a string like "aba"?

[1] [https://medium.com](https://medium.com/@kapoorprakhar99/next-permutation-b0c1c392556b)
[2] [https://learncodingfast.com](https://learncodingfast.com/leetcode-jump-game-python-solution/)
[3] [https://learn.lushaylabs.com](https://learn.lushaylabs.com/tang-nano-9k-first-processor/)
[4] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/dsa/lexicographic-permutations-of-string/)
[5] [https://algo.monster](https://algo.monster/liteproblems/1087)
[6] [https://codeforces.com](https://codeforces.com/problemset/problem/1609/B)
[7] [https://algo.monster](https://algo.monster/liteproblems/2657)
[8] [https://algo.monster](https://algo.monster/liteproblems/992)
[9] [https://medium.com](https://medium.com/nerd-for-tech/next-smaller-element-in-an-array-3198c64b5933)
[10] [https://stemhash.com](https://stemhash.com/efficient-permutations-in-lexicographic-order/)
[11] [https://www.hello-algo.com](https://www.hello-algo.com/en/chapter_sorting/quick_sort/)
[12] [https://medium.com](https://medium.com/womenintechnology/technical-interviews-everything-you-need-to-master-two-pointers-c21626667831)
[13] [https://algo.monster](https://algo.monster/liteproblems/2839)
[14] [https://medium.com](https://medium.com/@ankitviddya/dsa-problem-permutations-20c075f88d17)
[15] [https://www.thinka.ai](https://www.thinka.ai/en-US/Oxford-AQA-International-A-level/Computer-Science-9645/Stacks)
