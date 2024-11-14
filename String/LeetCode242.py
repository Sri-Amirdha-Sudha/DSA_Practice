# 242. Valid Anagram
"""
Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        countS ={}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[s[i]] = 1+countT.get(t[i],0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True