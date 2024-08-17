#!/usr/bin/python3

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)  # Convert jewels to a set for O(1) lookups
        count = 0
        for stone in stones:
            if stone in jewel_set:
                count += 1  
        return count
