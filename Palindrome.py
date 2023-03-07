# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 11:19:16 2023

@author: willh
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        converted_x = str(x)
        max_len = len(converted_x)
        i = 0
        for i in range(len(converted_x)):
            if (converted_x[i] == converted_x[max_len-1]):
                i = i + 1
                max_len = max_len - 1
            elif (converted_x[i] != converted_x[max_len-1]):
                return False
        return True