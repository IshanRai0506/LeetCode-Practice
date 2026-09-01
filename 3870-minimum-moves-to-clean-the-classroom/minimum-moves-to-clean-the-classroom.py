from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_id = {}
        k = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = k
                    k += 1

        target = (1 << k) - 1

        # best[r][c][mask] = maximum energy with which
        # we've reached (r,c) having collected 'mask'
        best = [
            [[-1] * (1 << k) for _ in range(n)]
            for _ in range(m)
        ]

        sr, sc = start

        q = deque()
        q.append((sr, sc, energy, 0, 0))
        best[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, e, mask, moves = q.popleft()

            if mask == target:
                return moves

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if classroom[nr][nc] == 'X':
                    continue

                if e == 0:
                    continue

                ne = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    new_mask |= 1 << litter_id[(nr, nc)]

                # Reset energy
                if classroom[nr][nc] == 'R':
                    ne = energy

                # If we've already reached this position with
                # the same mask and >= energy, this state is useless.
                if best[nr][nc][new_mask] >= ne:
                    continue

                best[nr][nc][new_mask] = ne
                q.append((nr, nc, ne, new_mask, moves + 1))

        return -1