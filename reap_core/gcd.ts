// Implements the GCD algorithmn for two string

function gcdOfStrings(str1: string, str2: string): string {
  const str1_length = str1.length;
  const str2_length = str2.length;

  let larger_length = 0;
  let smaller_length = 0;

  // set a to the higher length, b to the lesser
  if (str1_length > str2_length) {
    larger_length = str1_length;
    smaller_length = str2_length;
  } else {
    larger_length = str2_length;
    smaller_length = str1_length;
  }

  let temp = 0;

  // we keep dividing until the smallest number is 0
  while (smaller_length !== 0) {
    // store smallest length temporary as we need it to identify the last smallest
    // length which upon division becomes the new larger length
    temp = smaller_length;

    // modulus a % b with A always being the larger length
    smaller_length = larger_length % smaller_length;

    // set old smallest length as the larger length now
    larger_length = temp;
  }

  const str1_repeatable = str1_length / larger_length;
  const str2_repeatable = str2_length / larger_length;

  const sub_string = str1.substring(0, larger_length);

  if (
    sub_string.repeat(str1_repeatable) == str1 &&
    sub_string.repeat(str2_repeatable) == str2
  ) {
    return sub_string;
  }

  return "";
}

console.log("GCD: ", gcdOfStrings("ABABAB", "AB"));

console.log("GreatestDividingString: value=", gcdOfStrings("ABCABC", "ABC"));
console.log("GreatestDividingString: value=", gcdOfStrings("ABABAB", "AB"));
console.log("GreatestDividingString: value=", gcdOfStrings("LEET", "CODE"));
console.log("GreatestDividingString: value=", gcdOfStrings("AAAAAB", "AAA"));

console.log("GreatestDividingString: value=", gcdOfStrings("XYZXYZ", "XYZ"));
console.log("GreatestDividingString: value=", gcdOfStrings("ABCABCA", "ABC"));
console.log("GreatestDividingString: value=", gcdOfStrings("AAAAAA", "AA"));
console.log(
  "GreatestDividingString: value=",
  gcdOfStrings("ABCDEFABCDEF", "ABCXYZ"),
);
console.log("GreatestDividingString: value=", gcdOfStrings("ABBAABBA", "ABBA"));
console.log("GreatestDividingString: value=", gcdOfStrings("ABAB", "ABAC"));

console.log(
  "GreatestDividingString: value=",
  gcdOfStrings(
    "TAUXXTAUXXTAUXXTAUXXTAUXX",
    "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX",
  ),
);
