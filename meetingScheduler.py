"""
Availability slots:
- look for span of overlap
[  [10,50], [60,120], [140,210]]
[[0,15],    [60,70]]
duration = 8
  
steps:
1. sort according to start - "earliest time"
2. trim any windows smaller than duration 
3. walk through heap and check for condition
condiiton_overlap: min(end2, end1) - max(start2, start1) > 0 (if they overlap at all, )
                                                         > duration for this partcular case
test case:
assert x_i < x_i + 1 for x in each sequence (e.g windows are non-overalpping)
[10,    50]
  [20,30]       max(start), min(end)
  
  [20,  50]     max(start), min(end)
[10,  30]

assert overlap exists 
"""
from typing import Tuple, List

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], 
                                   slots2: List[List[int]], 
                                   duration: int) -> List[int]:
        self.slots1, self.slots2, self.duration = slots1, slots2, duration
        slots = self.filter_slots()
        
        while len(slots) > 1:
            slot1 = heappop(slots)  # grab leftmost interval
            slot0 = slots[0]        # compare this to the closest possible overlapping interval
            
            if self.isOverlap(slot0, slot1):
                return slots[0][0] + duration
        
        return []    
        
    def filter_slots(self) -> List[List[int]]:
        slots = self.sort_by_start()
        return list(filter(lambda slot: slot[1] - slot[0] < self.duration, slots))
    
    def sort_by_start(self) -> List[List[int]]: 
        #can combine both lists because they do not overalp
        return sorted(self.slots1 + self.slots2, key = lambda slot: slot[0])
    
    def isOverlap(self, slot0: List[int], slot1: List[int]) -> bool:
        return min(slot1[1], slot[1]) - max(slot1[0], slot[0]) >= self.duration

#Run Test:
slots1 = [[10,50],[60,120],[140,210]]
slots2 = [[0,15],[60,70]]
duration = 8
S = Solution()
#assert S.minAvailableDuration(slots1, slots2, duration) == [60,68], "base case" 
#assert S.minAvailableDuration(slots1, slots2, duration) == [], "non-overlap" 
#assert S.minAvailableDuration(slots1, slots2, duration) == [], "empty" 
