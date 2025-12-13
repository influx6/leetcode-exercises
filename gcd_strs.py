
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        str1_len = len(str1)
        str2_len = len(str2)
        a = b = 0

        # set correct GCD value setup
        if str1_len > str2_len:
            a = str1_len
            b = str2_len
        else:
            a = str2_len
            b = str1_len

        # GCD(a=6, b=3) where:
        #
        # First pass: b2 = GCD(b1, b1 mod a)
        #
        # So: b2 = GCD(6,3)
        #
        # Second pass: b3 = GCD(b1, b2 mod b1)
        #
        # Third pass: b4 = GCD(b3, b3 mod b2)
        #
        # repeat until b == 0
        while b != 0:
            # store be in temp var
            temp = b
            # first pass: GCD(b, b mod a)
            b = a % temp
            # a is now the previous value of b
            a = temp

        result = str1[0:a]

        print("GCD({}, {}, value=(a={}, b={})) = {}".format(str1, str2,a, b, result))

        # validation check
        str1_repeat = int(str1_len / a)
        validate_str1 = (result * str1_repeat) == str1;

        str2_repeat = int(str2_len / a)
        validate_str2 = (result * str2_repeat) == str2;

        if validate_str1 and validate_str2:
            return result
        else:
            return ""

print("GreatestDividingString: value=", gcdOfStrings("ABCABC", "ABC"))
print("GreatestDividingString: value=", gcdOfStrings("ABABAB", "AB"))
print("GreatestDividingString: value=", gcdOfStrings("LEET", "CODE"))
print("GreatestDividingString: value=", gcdOfStrings("AAAAAB", "AAA"))

print("GreatestDividingString: value=", gcdOfStrings("XYZXYZ", "XYZ"))
print("GreatestDividingString: value=", gcdOfStrings("ABCABCA", "ABC"))
print("GreatestDividingString: value=", gcdOfStrings("AAAAAA", "AA"))
print("GreatestDividingString: value=", gcdOfStrings("ABCDEFABCDEF", "ABCXYZ"))
print("GreatestDividingString: value=", gcdOfStrings("ABBAABBA", "ABBA"))
print("GreatestDividingString: value=", gcdOfStrings("ABAB", "ABAC"))

print("GreatestDividingString: value=", gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
