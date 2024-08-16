#!/usr/bin/python3
class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        if s.islower():
            for i in range(len(s) - 1):
                j = i + 1
                score += abs(ord(s[i]) - ord(s[j]))
                
        return score
