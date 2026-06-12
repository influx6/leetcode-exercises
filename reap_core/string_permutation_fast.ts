function string_permutation(text: string) {
  // split and sort the string into parts but in alphebetic order.
  // space complex is now O(n) since we are now storing in a list.
  // time compelexity is still O(n * n!) where n! is n factorial
  const sorted = text.split("").sort();

  // helps us identify which of the string in the list is now
  // used in the run.
  const used = new Array(sorted.length).fill(false);
  const current: string[] = [];

  function backtrack() {
    if (current.length === sorted.length) {
      console.log(current);
      return;
    }

    // this is doing an O(n) loop
    for (let index = 0; index < sorted.length; index++) {
      // if we've used the index via the mask(boolean)
      // then we skip it, important since we will do
      // another recursive backtrack with the same variables
      // instead of cloning them.
      if (used[index]) continue;

      // block index as used, so next turn skips
      used[index] = true;
      // store the current char
      current.push(sorted[index]);

      // run re-cursive for current permutation
      backtrack();

      // unblock char as used, since its turn has ended
      used[index] = false;
      // remove it from char list
      current.pop();
    }
  }

  // computation time complexity is a O(n * n!)
  backtrack();
}

string_permutation("abc");
string_permutation("aac");
// string_permutation("remember");
