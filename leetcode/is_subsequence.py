class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        print("Incoming: ", s, t)
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False

        found = 0
        for index in range(len(t)):
            if found >= len(s):
                break
            if t[index] == s[found]:
                found += 1
                continue

        return found >= len(s)


solution = Solution()
print("IsSubsequence: ", solution.isSubsequence("aab", "abcabcabc"))
print("IsSubsequence: ", solution.isSubsequence("aaa", "abcabcbc"))
print("IsSubsequence: ", solution.isSubsequence("abc", "ahbgdc"))
