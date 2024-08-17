#!/usr/bin/python3

class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        if len(s) != len(t):
            raise ValueError("Strings s and t must be of the same length.")
        
        D = {}
        sum_diff = 0
        
        for i in range(len(s)):
            D[s[i]] = i
        
        for i in range(len(t)):
            if t[i] not in D:
                raise ValueError(f"Character '{t[i]}' in t not found in s.")
            sum_diff += abs(i - D[t[i]])
        
        return sum_diff
