from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) <= 1:
            return len(chars)

        read = 0 # index pointing at where we've read to in the chars
        write = 0 # point to where we want to write from
        total = len(chars)

        while read < total:
            count = 0
            char = chars[read]
            while read < total and chars[read] == char:
                count += 1
                read += 1

            chars[write] = char
            write += 1

            if count > 1:
                for size in str(count):
                    chars[write] = size
                    write += 1

        return write



solution = Solution()
print("NewLength: ", solution.compress(list("aaaaabbbbbcdddd")))
print("NewLength: ", solution.compress([]))
print("NewLength: ", solution.compress(list("a")))
print("NewLength: ", solution.compress(list("acdacdacdacd")))
print("NewLength: ", solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
