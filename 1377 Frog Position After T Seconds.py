class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        def is_relevant_edge(node, edge, visited):
            for pair in [edge, [edge[1], edge[0]]]:
                if pair[0] == node and pair[1] not in visited:
                    return True

        def fetch_other(node, edge):
            if edge[0] == node:
                return edge[1]
            else:
                return edge[0]

        current = [[1]]
        visited = set()
        counts = [1] * (n + 1)
        
        for _ in range(t):
            next_batches = []
            for batch in current:
                for node in batch:
                    visited.add(node)

                    children = [fetch_other(node, edge) for edge in edges if is_relevant_edge(node, edge, visited)]

                    if children:
                        for child in children:
                            counts[child] = counts[node] * len(children)

                        next_batches.append(children)
                    else:
                        next_batches.append([node])
            current = next_batches

        for batch in current:
            for node in batch:
                if node == target:
                    return 1 / counts[node]
        else:
            return 0
