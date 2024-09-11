from collections import defaultdict, deque


class Node:
    def __init__(self, val: int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def solution(root: Node):
    hmap = defaultdict(list)
    min_x, max_x = 0, 0
    queue = deque([(root, 0)])

    while queue:
        node, x = queue.popleft()
        min_x, max_x = min(min_x, x), max(max_x, x)
        hmap[x].append(node.val)

        if node.left:
            queue.append((node.left, x - 1))
        if node.right:
            queue.append((node.right, x + 1))

    res = []
    for idx in range(min_x, max_x + 1):
        res.append(hmap[idx])

    return res


def test():
    assert solution(Node(3, Node(9), Node(20, Node(15), Node(7)))) == [
        [9],
        [3, 15],
        [20],
        [7],
    ]
