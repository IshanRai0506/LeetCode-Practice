from typing import List

class Solution:
    def palindromePath(
        self, n: int, edges: List[List[int]],
        s: str, queries: List[str]
    ) -> List[bool]:

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        LOG = n.bit_length()
        parent = [[0] * n for _ in range(LOG)]
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n

        timer = 0
        stack = [(0, -1, 0)]

        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                parent[0][u] = u if p == -1 else p
                stack.append((u, p, 1))

                for v in reversed(adj[u]):
                    if v != p:
                        depth[v] = depth[u] + 1
                        stack.append((v, u, 0))
            else:
                tout[u] = timer - 1

        for k in range(1, LOG):
            for u in range(n):
                parent[k][u] = parent[k - 1][
                    parent[k - 1][u]
                ]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]
            for k in range(LOG):
                if diff & (1 << k):
                    u = parent[k][u]

            if u == v:
                return u

            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    u = parent[k][u]
                    v = parent[k][v]

            return parent[0][u]

        bit = [0] * (n + 2)

        def add(i, value):
            i += 1
            while i <= n + 1:
                bit[i] ^= value
                i += i & -i

        def point_query(i):
            i += 1
            result = 0
            while i > 0:
                result ^= bit[i]
                i -= i & -i
            return result

        current = [1 << (ord(c) - ord('a')) for c in s]
        root_mask = [0] * n
        stack = [(0, -1, 0)]

        while stack:
            u, p, mask = stack.pop()
            root_mask[u] = mask ^ current[u]

            for v in adj[u]:
                if v != p:
                    stack.append((v, u, root_mask[u]))

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                u = int(parts[1])
                new_mask = 1 << (ord(parts[2]) - ord('a'))
                delta = current[u] ^ new_mask

                if delta:
                    add(tin[u], delta)
                    add(tout[u] + 1, delta)

                current[u] = new_mask

            else:
                u = int(parts[1])
                v = int(parts[2])

                mu = root_mask[u] ^ point_query(tin[u])
                mv = root_mask[v] ^ point_query(tin[v])
                w = lca(u, v)

                path_mask = mu ^ mv ^ current[w]

                answer.append(
                    path_mask == 0 or
                    (path_mask & (path_mask - 1)) == 0
                )

        return answer