#!/usr/bin/python3

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_len = 0
        for sentence in sentences:
            words = sentence.split()
            if len(words) > max_len:
                max_len = len(words)
        return max_len