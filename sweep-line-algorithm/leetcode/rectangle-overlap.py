# Source: https://leetcode.com/problems/rectangle-overlap/
# Problem: 836. Rectangle Overlap
# Data Structure: Sweep Line Algorithm
# Difficult: Easy
# Autores: Giovanne Santos, Marlus Marcos, Thiago Silva, Yan Carlos
# Created on 2019/09/26

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        horiz_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
        vert_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
        return horiz_overlap and vert_overlap
