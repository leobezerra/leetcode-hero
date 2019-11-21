# Source: https://leetcode.com/problems/rectangle-area/
# Problem: 223. Rectangle Area
# Data Structure: Sweep Line Algorithm
# Difficult: Medium
# Autores: Giovanne Santos, Marlus Marcos, Thiago Silva, Yan Carlos
# Created on 2019/09/26

def isRectangleOverlap(rec1: List[int], rec2: List[int]) -> bool:
    horiz_overlap = max(rec1[0], rec2[0]) < min(rec1[2], rec2[2])
    vert_overlap = max(rec1[1], rec2[1]) < min(rec1[3], rec2[3])
    return horiz_overlap and vert_overlap

def isRectangleContains(rec1: List[int], rec2: List[int]) -> bool:
    horiz_contains = rec1[0] == min(rec1[0], rec2[0]) and rec1[2] == max(rec1[2], rec2[2])
    vert_contains = rec1[1] == min(rec1[1], rec2[1]) and rec1[3] == max(rec1[3], rec2[3])
    return horiz_contains and vert_contains
  
  
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rec1 = [A,B,C,D]
        rec2 = [E,F,G,H]
        rec1_area = (C - A) * (D - B)
        rec2_area = (G - E) * (H - F)
        overlap = isRectangleOverlap(rec1, rec2)
        if not overlap:
            return rec1_area + rec2_area
        else:
            if isRectangleContains(rec1, rec2):
                return rec1_area
            if isRectangleContains(rec2, rec1):
                return rec2_area
            
            return rec1_area + rec2_area - (min(C,G) - max(A,E)) * (min(D,H) - max(B,F))
            total = (max(C,G) - min(A,E)) * (max(D,H) - min(B,F))
            total -= (max(A,E) - min(A,E)) * (max(B,F) - min(B,F))
            total -= (max(C,G) - min(C,G)) * (max(D,H) - min(D,H))
            return total
