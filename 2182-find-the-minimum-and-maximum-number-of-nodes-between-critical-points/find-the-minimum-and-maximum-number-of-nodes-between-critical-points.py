# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Initialize pointers
        prev, curr = head, head.next
        index = 1  # start from second node
        critical_points = []
        
        # Traverse until the second last node
        while curr and curr.next:
            nxt = curr.next
            # Check local maxima/minima
            if (curr.val > prev.val and curr.val > nxt.val) or (curr.val < prev.val and curr.val < nxt.val):
                critical_points.append(index)
            
            # Move forward
            prev, curr = curr, nxt
            index += 1
        
        # If fewer than 2 critical points
        if len(critical_points) < 2:
            return [-1, -1]
        
        # Compute minDistance and maxDistance
        minDist = min(b - a for a, b in zip(critical_points, critical_points[1:]))
        maxDist = critical_points[-1] - critical_points[0]
        
        return [minDist, maxDist]

