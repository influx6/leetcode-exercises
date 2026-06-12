This is another foundational Prefix Sum problem, commonly known as Find Pivot Index. The goal is to find a balancing point in the array where the total weight of the numbers on the left equals the total weight of the numbers on the right.
## 1. Understand the Problem
Imagine a balance scale. You want to pick one index (the pivot) to act as the center.

* The Left Sum is the total of all numbers before that index.
* The Right Sum is the total of all numbers after that index.
* The number at the pivot index itself is ignored in both sums.
* If you check from left to right, return the very first index where Left Sum == Right Sum.

## 2. The Clever Mathematical Trick (Prefix Sum)
A beginner might think: "At every index, I should use a loop to calculate the left sum, and another loop to calculate the right sum."
Doing that takes too long. If the array has 10,000 numbers, checking every single index that way requires millions of calculations.
Instead, we use a simple math pattern:
$$\text{Right Sum} = \text{Total Sum} - \text{Left Sum} - \text{Current Number}$$ 
Because of this formula, if we know the Total Sum of the array, we can track the Left Sum as we walk through the array and instantly calculate the Right Sum without extra loops!
## 3. Visualize with an Example
Let's use Example 1: nums = [1, 7, 3, 6, 5, 6]

* Step 1: Calculate the total_sum.
$$1 + 7 + 3 + 6 + 5 + 6 = 28$$ 
* Step 2: Start walking through the array from index 0. Keep track of left_sum (starts at $0$).

| Index | Current Number | Left Sum | Formula: total_sum - left_sum - current | Right Sum | Match? |
|---|---|---|---|---|---|
| 0 | 1 | 0 | $28 - 0 - 1$ | 27 | ❌ $0 \neq 27$ |
| 1 | 7 | $0 + 1 = \mathbf{1}$ | $28 - 1 - 7$ | 20 | ❌ $1 \neq 20$ |
| 2 | 3 | $1 + 7 = \mathbf{8}$ | $28 - 8 - 3$ | 17 | ❌ $8 \neq 17$ |
| 3 | 6 | $8 + 3 = \mathbf{11}$ | $28 - 11 - 6$ | 11 | ** 11 == 11** |

We found a match at Index 3! We immediately return 3.
## 4. Step-by-Step Code Logic## Step 1: Sum the Array
Get the total sum of all numbers in the input array using a built-in sum function.
## Step 2: Initialize Left Sum
Create a variable left_sum and set it to $0$.
## Step 3: Loop and Check
Loop through the array using both the index and the value. At each step, check if left_sum is exactly equal to total_sum - left_sum - current_value. If it matches, immediately return the current index.
## Step 4: Update Left Sum
If it does not match, add the current value to left_sum before moving to the next index.
## Step 5: Return Default
If the loop finishes and no match is found, return $-1$.
------------------------------
## 5. Code Implementation
Here is the clean, efficient solution in Python:

def pivotIndex(nums: list[int]) -> int:
    total_sum = sum(nums)
    left_sum = 0
    
    for i, num in enumerate(nums):
        # Check if the left side matches the calculated right side
        if left_sum == (total_sum - left_sum - num):
            return i
        
        # Add the current number to left_sum for the next iteration
        left_sum += num
        
    return -1

## 6. Complexity Analysis

* Time Complexity: $\mathcal{O}(n)$. We loop through the array once to find the total_sum, and once more to find the pivot. This is incredibly fast.
* Space Complexity: $\mathcal{O}(1)$. We only use a couple of variables to store the sums, meaning no extra memory is taken up.

------------------------------
## ✅ Final Answer
The leftmost pivot index is found by calculating the total sum upfront, then scanning the array linearly while comparing the rolling left sum to the remaining right sum.
Would you like to try a practice problem that uses this exact same logic, or would you like to see this code written in Java / C++?


Your TypeScript/JavaScript implementation is excellent and 100% correct! You perfectly translated the prefix sum logic into clean, readable code.
However, there is one small hidden edge case in JavaScript/TypeScript's reduce() function that could cause your code to crash in an actual interview or coding platform.
## ⚠️ The Hidden Bug: Empty Arrays
If the input array nums is empty [], your code will throw a runtime error:
TypeError: Reduce of empty array with no initial value.
In JavaScript, if you don't provide an initial value (like 0) to reduce(), it uses the first element of the array. If the array has no elements, it crashes. The problem constraints state 1 <= nums.length, so it passes here, but it is always best practice to provide 0 as the initial value to prevent crashes and ensure type safety.
------------------------------
## 🛠️ Optimized and Bulletproof Version
Here is your exact code with that small fix added to the reduce function, along with proper TypeScript types:

function pivot_index(nums: number[]): number {
  // Added ', 0' at the end to safely handle empty arrays and enforce types
  const total_sum = nums.reduce((acc, current) => acc + current, 0); 

  let left_sum = 0;
  
  for (let index = 0; index < nums.length; index++) {
    const value_at_index = nums[index];
    const right_sum = total_sum - left_sum - value_at_index;
    
    if (right_sum === left_sum) { // Used strict equality (===)
      return index;
    }
    
    left_sum += value_at_index;
  }

  return -1;
}

console.log(pivot_index([1, 7, 3, 6, 5, 6])); // Output: 3

## Why these minor changes matter:

   1. , 0 in reduce: Ensures that if nums is empty, total_sum safely becomes 0 instead of breaking.
   2. === instead of ==: In JavaScript/TypeScript, always prefer strict equality (===) to avoid accidental type coercion bugs.

------------------------------
## ✅ Code Review Verdict
Your logic is flawless, your variable names (value_at_index, right_sum, left_sum) make the code incredibly self-explanatory, and the performance is an optimal $\mathcal{O}(n)$ time and $\mathcal{O}(1)$ space. Great job!
Would you like to move on to a slightly harder Prefix Sum interview problem, like finding the Subarray Sum Equals K, or would you like to review Prefix Sum arrays where we store all sums upfront?
