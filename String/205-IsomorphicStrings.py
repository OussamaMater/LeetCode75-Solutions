"""
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        dict_1 = {}
        dict_2 = {}

        # If the key exists and the saved mapping does not match the current one, we return False
        for i, j in zip(s, t):
            if ((i in dict_1) and (dict_1[i] != j)) or (
                (j in dict_2) and (dict_2[j] != i)
            ):
                return False

            # Otherwise we'll create a new mapping
            dict_1[i] = j
            dict_2[j] = i

        # At this point we are sure that there are only unique mappings
        return True


# Running TestCase
solution = Solution()
print(solution.isIsomorphic("egg", "add"))
