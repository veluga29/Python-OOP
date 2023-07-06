from typing import Optional


class Node:
    def __init__(self, data: int, node: Optional["Node"]):
        self.data = data
        self.node = node


node2 = Node(2, None)
node1 = Node(1, node2)
node0 = Node(0, node1)
