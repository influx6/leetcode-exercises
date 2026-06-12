function backtrack(current: string, remaining: Array<String>) {
  if (remaining.length === 0) {
    console.log(current);
    return;
  }

  // this is doing an O(n) loop
  for (let index = 0; index < remaining.length; index++) {
    // if we are at a greater index and the current index letter is the same as the last index, meaning we've finished  the turn of the first, then skip - how ?
    // Because remaining now has the previous letter that was previously filtered out back in the list.
    if (index > 0 && remaining[index] == remaining[index - 1]) {
      continue;
    }

    const nextChar = remaining[index];

    // this is making O(n) x length of remaining, so basic n! factorial
    backtrack(
      current + nextChar,
      // another O(n) space complexity for every list we create
      remaining.filter((_, rindex) => rindex !== index),
    );
  }
}

function string_permutation(text: string) {
  // split and sort the string into parts but in alphebetic order.
  // space complex is now O(n) since we are now storing in a list.
  const sorted = text.split("").sort();

  // computation time complexity is a O(n * n!)
  backtrack("", sorted);
}

string_permutation("abc");
string_permutation("aac");
