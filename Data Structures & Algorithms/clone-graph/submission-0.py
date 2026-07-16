"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Map original node to clone nodes
        hashmap = {}

        def hash_graph(node):
            hashmap[node] = Node(node.val)
            for neighbor in node.neighbors:
                if neighbor not in hashmap:
                    hash_graph(neighbor)

        hash_graph(node)

        visited = set()
        def connect_graph(node):
            clone = hashmap[node]
            visited.add(node)
            for neighbor in node.neighbors:
                clone.neighbors.append(hashmap[neighbor])
                if neighbor not in visited:
                    connect_graph(neighbor)

        connect_graph(node)
        return hashmap[node]
            
