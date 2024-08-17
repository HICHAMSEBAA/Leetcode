#!/usr/bin/python3

class Solution:
    def defangIPaddr(self, address: str) -> str:
        list_1 = address.split(".")
        list_2 = []
        for i in range(len(list_1)):
            if i < len(list_1) - 1:
                list_2.append(list_1[i] + "[.]")
            else:
                list_2.append(list_1[i])
        return "".join(list_2)
