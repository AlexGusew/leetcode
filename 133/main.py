"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional

class Solution:
    def clone(self, original, new, visited):
        visited.add(original.val)
        for nei in original.neighbors:
            if nei in visited:
                continue
            new_nei = Node(nei.val)
            new.neighbors.add(new_nei)
            new_nei.neighbors.add(new)
            self.clone(nei, new_nei, visited;
        return new

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.clone(node, Node(node.val), set())
