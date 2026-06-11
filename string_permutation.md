The snippet you shared is an excellent, textbook example of recursive backtracking. It ensures a clean, alphabetical output by sorting the characters before making any decisions.
Here is a breakdown of how this code works, why it works, and how to analyze its performance.
------------------------------
## 🔍 How It Works Under the Hood
The algorithm uses a decision tree approach. At every step, it chooses one available character, adds it to the current build, and repeats the process with the remaining characters.
## 1. The Pre-Sort Trick

const sortedChars = str.split('').sort();

By sorting "cba" into ['a', 'b', 'c'] at the very beginning, the loop is guaranteed to pick the alphabetically smallest available character first. Because recursion explores choices from left to right, the final outputs naturally emerge in strict lexicographical order.
## 2. The Backtracking Loop

for (let i = 0; i < remaining.length; i++) {
  const nextChar = remaining[i];
  const nextRemaining = remaining.filter((_, idx) => idx !== i);
  backtrack(current + nextChar, nextRemaining);
}


* Choose: It picks the character at index i.
* Explore: It filters that character out to create nextRemaining and passes it to the next recursive call.
* Unchoose (Implicit): When that recursive call finishes, the loop moves to index i + 1. The original remaining array stays untouched, effectively "undoing" the choice so a different character can be tried next.

## 3. The Base Case

if (remaining.length === 0) {
  console.log(current);
  return;
}

When there are no characters left to choose from, a complete permutation has been formed. The function prints it and stops digging deeper down that specific branch. [1, 2] 
------------------------------
## ⏱️ Complexity Analysis
Permutation problems grow incredibly fast. Interviewers will always ask you about the efficiency of this code.

* Time Complexity: $O(n \times n!)$
* There are $n!$ (n-factorial) total permutations.
   * At each leaf node of the recursion tree, it takes $O(n)$ time to print or manipulate the string.
   * Inside the loop, .filter() takes $O(n)$ time. [3] 
* Space Complexity: $O(n^2)$ or $O(n)$
* The recursion stack goes $n$ levels deep (the length of the string).
   * However, because this specific implementation creates a brand-new nextRemaining array using .filter() at every single step, it allocates $O(n)$ extra memory per level, leading to $O(n^2)$ total transient space. [4] 

------------------------------
## 🛠️ The "Pro" Interview Optimization
While the code you provided is perfectly correct, using .filter() inside a loop creates a lot of unnecessary arrays. In a high-pressure interview, an interviewer might ask: "Can you optimize this to use less memory?"
You can optimize it to $O(n)$ space by using an array of booleans to track which characters have been "used" instead of slicing or filtering the array. [5] 

function printPermutationsOptimized(str: string): void {
  const sorted = str.split('').sort();
  const used = new Array(str.length).fill(false);
  const current: string[] = [];

  function backtrack(): void {
    if (current.length === str.length) {
      console.log(current.join(''));
      return;
    }

    for (let i = 0; i < sorted.length; i++) {
      if (used[i]) continue; // Skip already chosen characters

      // 1. Choose
      used[i] = true;
      current.push(sorted[i]);

      // 2. Explore
      backtrack();

      // 3. Unchoose (Explicit Backtracking)
      current.pop();
      used[i] = false;
    }
  }

  backtrack();
}

------------------------------
If you want to practice further, tell me if you would like to:

* See how to modify this to handle duplicate characters (e.g., inputting "aab" without printing duplicates).
* Convert this solution into an iterative approach.
* Solve a related problem like combinations or subsets. [6] 


[1] [https://www.naukri.com](https://www.naukri.com/code360/problem-details/permutations-of-a-string_985254)
[2] [https://www.geeksforgeeks.org](https://www.geeksforgeeks.org/javascript/javascript-program-to-print-all-permutations-of-given-string/)
[3] [https://medium.com](https://medium.com/softaai-blogs/how-to-generate-all-permutations-of-a-string-in-kotlin-fast-o-n-approach-handles-duplicates-b2a4eaf04cde)
[4] [https://www.scribd.com](https://www.scribd.com/document/979300441/TCS-TAG-2025-Recursion-Problems-Actual-Exam)
[5] [https://medium.com](https://medium.com/@kumarsuraj19111997/how-to-generate-all-permutations-of-a-string-in-swift-with-state-space-tree-355a56825d7b)
[6] [https://medium.com](https://medium.com/softaai-blogs/how-to-generate-all-permutations-of-a-string-in-kotlin-fast-o-n-approach-handles-duplicates-b2a4eaf04cde)

To handle duplicates in the first version (the one using .filter()), you need to add a single condition inside the loop: skip the current character if it is the same as the previous character in that same loop. [1] 
Because the array is already sorted, duplicate characters sit right next to each other (e.g., ['a', 'a', 'b']). Skipping adjacent duplicates prevents the algorithm from spawning identical execution branches. [2, 3, 4] 
## 🛠️ The Duplicate-Safe Version
Here is how you modify the first version to handle strings like "aab" safely:

function printPermutationsWithDuplicates(str: string): void {
  // Step 1: Sorting places duplicates next to each other
  const sortedChars = str.split('').sort();

  function backtrack(current: string, remaining: string[]): void {
    if (remaining.length === 0) {
      console.log(current);
      return;
    }

    for (let i = 0; i < remaining.length; i++) {
      // CRITICAL CHECK: If this char matches the previous one in this loop, skip it
      if (i > 0 && remaining[i] === remaining[i - 1]) {
        continue; 
      }

      const nextChar = remaining[i];
      const nextRemaining = remaining.filter((_, idx) => idx !== i);

      backtrack(current + nextChar, nextRemaining);
    }
  }

  backtrack("", sortedChars);
}

printPermutationsWithDuplicates("aab");// Output: "aab", "aba", "baa" (No duplicates!)

## 🧠 Why This Works
Imagine you pass "aab" into this function. The initial remaining array is ['a₁', 'a₂', 'b'].

   1. First iteration (i = 0): The loop picks a₁. The remaining items are ['a₂', 'b']. Recursion continues normally down this branch.
   2. Second iteration (i = 1): The loop wants to pick a₂. But the code checks remaining[1] === remaining[0] (a₂ === a₁).
   3. The Skip: Because they are identical, the loop executes continue. It skips a₂ entirely and jumps straight to b (i = 2). [5] 

By skipping a₂ at the root level, you prevent an entire redundant subtree—such as a₂ -> a₁ -> b—from ever being calculated.
------------------------------
Would you like to:

* See a visual tree diagram of how the duplicate skipping cuts off redundant branches?
* Learn how to implement this duplicate check in the optimized boolean array version?
* Explore how to solve this using a Frequency Map (Hash Map) instead of sorting?


[1] [https://medium.com](https://medium.com/@sheefanaaz6417/40-combination-sum-ii-f418a7043b86)
[2] [https://algo.monster](https://algo.monster/liteproblems/217)
[3] [https://algo.monster](https://algo.monster/liteproblems/26)
[4] [https://teebowblogs.medium.com](https://teebowblogs.medium.com/my-harvard-cs50-notes-lecture-3-algorithms-09d11ab12ad9)
[5] [https://algo.monster](https://algo.monster/liteproblems/717)

It is completely understandable why this looks contradictory at first glance! It feels like we are skipping the second 'a' entirely.
The secret lies in the phrase "in this loop."
We only skip the second 'a' when it tries to act as the leader of a new branch at the same level. We do not skip it when it is passed down deeper into the next recursive call.
Here is the exact difference between what is blocked and what is allowed.
------------------------------
## 🟢 1. Moving Deeper (Allowed)
When i = 0, the loop picks the first 'a'.

* The code creates nextRemaining = ['a', 'b'] (using the index filter).
* It immediately calls backtrack("a", ['a', 'b']).
* Inside that next recursive call, a brand-new loop starts. That loop sees remaining = ['a', 'b']. It picks the remaining 'a' perfectly fine because i = 0 at the start of that new loop.

This is how we successfully get "aab".
## 🔴 2. Moving Horizontally in the Same Loop (Blocked)
The duplicate check only triggers when the current loop finishes dealing with the first 'a' and moves sideways to i = 1.
At this point, the current loop is asking: "Hey, I just finished exploring every single word that starts with 'a'. Should I now explore every single word that starts with this second 'a'?"
The duplicate check steps in and says: "No. Starting a new branch with the second 'a' will give you the exact same results as the branch you just finished with the first 'a'."
------------------------------
## 🗺️ The Execution Tree
Look at how the choices branch out for ['a₁', 'a₂', 'b']:

                      [Root]
         /              |             \
     i = 0            i = 1          i = 2
   Pick 'a₁'        Pick 'a₂'       Pick 'b'
     /                  |               \
['a₂', 'b']        ['a₁', 'b']      ['a₁', 'a₂']

     |                  |
  (Proceeds)         SKIPPED!
                 (Duplicates 'a₁' 
                  at root level)


* Vertical lines mean going deeper (passing the remaining characters down). The second 'a' is safely passed down here.
* Horizontal lines mean the loop is moving to the next index. The duplicate check only cuts off horizontal duplicates, ensuring we don't start the exact same sub-tree twice.

------------------------------
If you'd like to cement this, we can look at a step-by-step trace table showing the exact values of i, current, and remaining as the code runs, or we can look at how a Frequency Map completely removes the need for this index-skipping logic. Which sounds more helpful?
