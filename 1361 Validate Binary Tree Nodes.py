class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        from queue import SimpleQueue

        seen = set((0,))
        nodes = SimpleQueue()
        nodes.put(0)
        
        while not nodes.empty():
            node = nodes.get()
            for child in [leftChild[node], rightChild[node]]:
                if child == node:
                    return False

                if child in seen:
                    return False

                if child > 0:
                    seen.add(child)
                    nodes.put(child)

        all_nodes = set(leftChild) | set(rightChild)

        return all_nodes - seen <= {-1}
