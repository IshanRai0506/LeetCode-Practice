from collections import defaultdict, deque
from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Step 1: Build forward and reverse graphs
        forward = defaultdict(list)
        reverse = defaultdict(list)
        for a, b in invocations:
            forward[a].append(b)
            reverse[b].append(a)
        
        # Step 2: Find suspicious methods (reachable from k)
        suspicious = set()
        queue = deque([k])
        while queue:
            node = queue.popleft()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nei in forward[node]:
                if nei not in suspicious:
                    queue.append(nei)
        
        # Step 3: Check if removal is possible
        for s in suspicious:
            for caller in reverse[s]:
                if caller not in suspicious:
                    # Non-suspicious method calls suspicious → cannot remove
                    return list(range(n))
        
        # Step 4: Return remaining methods
        return [i for i in range(n) if i not in suspicious]
