class Solution:
    def reverseVowels(self, val: str) -> str:
        vowels = 'aeiouAEIOU'
        values = list(val)
        total = len(values)

        starter = 0
        ender = total - 1

        # print("Values: ", values, total, starter, ender)
        # for index in range(total):
        while starter < ender:
            # for each iteration: do only one operation, we enforce this with if..elif..else
            if values[starter] not in vowels:
                starter += 1
            elif values[ender] not in vowels:
                ender -= 1
            else:
                values[starter], values[ender] = values[ender], values[starter]
                starter += 1
                ender -= 1

        return ''.join(values)

def reverse_vowels(s):
    vals = list(s)
    vowels = 'aeiouAEIOU'
    left, right = 0, len(vals) - 1

    while left < right:
        if vals[left] not in vowels:
            left += 1
        elif vals[right] not in vowels:
            right -= 1
        else:
            vals[left], vals[right] = vals[right], vals[left]
            left += 1
            right -= 1
    return ''.join(vals)

assert reverse_vowels("IceCreAm") == "AceCreIm" # expect: AceCreIm
assert reverse_vowels2("IceCreAm") == "AceCreIm" # expect: AceCreIm

assert reverse_vowels("leetcode") == "leotcede" # expect: leotcede
assert reverse_vowels2("leetcode") == "leotcede" # expect: AceCreIm

assert reverse_vowels("MaMa") == "MaMa" # expect: MaMa
assert reverse_vowels("MAMa") == "MaMA" # expect: MaMA
assert reverse_vowels("MnMn") == "MnMn" # expect: MaMA
assert reverse_vowels("MNMn") == "MNMn" # expect: MaMA
assert reverse_vowels("MnMN") == "MnMN" # expect: MaMA
