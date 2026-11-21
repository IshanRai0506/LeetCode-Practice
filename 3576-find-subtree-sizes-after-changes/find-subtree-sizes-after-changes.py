class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        # Step 1: Find the closest ancestor with the same character
        stack = [(0, 0, False)]

        while stack:
            node, prev, exiting = stack.pop()

            if exiting:
                if prev == -1:
                    last.pop(s[node], None)
                else:
                    last[s[node]] = prev
                continue

            old = last.get(s[node], -1)

            if old != -1:
                new_parent[node] = old

            last[s[node]] = node

            stack.append((node, old, True))

            for child in children[node]:
                stack.append((child, 0, False))

        # Step 2: Build the modified tree
        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Step 3: Calculate subtree sizes
        answer = [1] * n
        stack = [(0, False)]

        while stack:
            node, visited = stack.pop()

            if not visited:
                stack.append((node, True))

                for child in new_children[node]:
                    stack.append((child, False))
            else:
                for child in new_children[node]:
                    answer[node] += answer[child]

        return answer