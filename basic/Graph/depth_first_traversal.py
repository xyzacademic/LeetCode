"""
Depth first traversal
"""
from basic.collection.stack import Stack


def dft(head=None):
    if not head:
        return
    
    results = []
    
    stack = Stack()
    stack.push(head)
    results.append(head.key)
    
    while not stack.is_empty():
        current_node = stack.pop()
        for neighbor in current_node.neighbors:
            if neighbor.key not in results:
                stack.push(current_node)
                stack.push(neighbor)
                results.append(neighbor.key)
                break