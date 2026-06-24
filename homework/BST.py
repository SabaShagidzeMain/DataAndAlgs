import sys

sys.setrecursionlimit(1_000_000)


class Node:
    __slots__ = ("val", "left", "right", "parent", "size", "height")

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.size = 1
        self.height = 1


class BST:
    def __init__(self):
        self.root = None

    @staticmethod
    def _update(node):
        if node is None:
            return
        left_size = node.left.size if node.left else 0
        right_size = node.right.size if node.right else 0
        node.size = 1 + left_size + right_size

        left_h = node.left.height if node.left else 0
        right_h = node.right.height if node.right else 0
        node.height = 1 + (left_h if left_h > right_h else right_h)

    def _update_up(self, node):
        while node:
            self._update(node)
            node = node.parent

    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return

        cur = self.root
        while True:
            if x < cur.val:
                if cur.left is None:
                    cur.left = Node(x)
                    cur.left.parent = cur
                    self._update_up(cur)
                    return
                cur = cur.left
            elif x > cur.val:
                if cur.right is None:
                    cur.right = Node(x)
                    cur.right.parent = cur
                    self._update_up(cur)
                    return
                cur = cur.right
            else:
                # duplicate, ignore
                return

    def _search_node(self, x):
        cur = self.root
        while cur:
            if x == cur.val:
                return cur
            if x < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def search(self, x):
        return self._search_node(x) is not None

    def _minimum(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, x):
        node = self._search_node(x)
        if node is None:
            return

        # Case 1: leaf
        if node.left is None and node.right is None:
            parent = node.parent
            if parent is None:
                self.root = None
            else:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                node.parent = None
                self._update_up(parent)
            return

        # Case 2: one child
        if node.left is None or node.right is None:
            child = node.left if node.left else node.right
            parent = node.parent
            if parent is None:
                self.root = child
                child.parent = None
            else:
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
                child.parent = parent
                self._update_up(parent)
            node.left = node.right = node.parent = None
            return

        # Case 3: two children
        successor = self._minimum(node.right)
        node.val = successor.val

        succ_parent = successor.parent
        succ_child = successor.right

        if succ_parent.left is successor:
            succ_parent.left = succ_child
        else:
            succ_parent.right = succ_child

        if succ_child:
            succ_child.parent = succ_parent

        successor.left = successor.right = successor.parent = None
        self._update_up(succ_parent)

    def kth(self, k):
        cur = self.root
        while cur:
            left_size = cur.left.size if cur.left else 0
            if k == left_size + 1:
                return cur.val
            if k <= left_size:
                cur = cur.left
            else:
                k -= left_size + 1
                cur = cur.right
        return None  # should not happen if k is valid

    def range(self, a, b):
        res = []

        def dfs(node):
            if node is None:
                return
            if node.val >= a:
                dfs(node.left)
            if a <= node.val <= b:
                res.append(node.val)
            if node.val <= b:
                dfs(node.right)

        dfs(self.root)
        return res

    def lca(self, a, b):
        node_a = self._search_node(a)
        node_b = self._search_node(b)
        if node_a is None or node_b is None:
            return None

        def depth(node):
            d = 0
            while node.parent:
                d += 1
                node = node.parent
            return d

        da = depth(node_a)
        db = depth(node_b)

        while da > db:
            node_a = node_a.parent
            da -= 1
        while db > da:
            node_b = node_b.parent
            db -= 1

        while node_a != node_b:
            node_a = node_a.parent
            node_b = node_b.parent

        return node_a.val

    def predecessor(self, x):
        cur = self.root
        pred = None
        while cur:
            if cur.val < x:
                pred = cur.val
                cur = cur.right
            else:
                cur = cur.left
        return pred

    def successor(self, x):
        cur = self.root
        succ = None
        while cur:
            if cur.val > x:
                succ = cur.val
                cur = cur.left
            else:
                cur = cur.right
        return succ

    def is_valid(self):
        stack = []
        cur = self.root
        prev = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if prev is not None and prev >= cur.val:
                return False
            prev = cur.val
            cur = cur.right
        return True

    def height(self):
        return self.root.height if self.root else 0

    def balance_report(self):
        def dfs(node):
            if node is None:
                return
            dfs(node.left)
            left_h = node.left.height if node.left else 0
            right_h = node.right.height if node.right else 0
            bf = left_h - right_h
            print(f"{node.val}, {node.height}, {node.size}, {bf}")
            dfs(node.right)

        dfs(self.root)


def main():
    bst = BST()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]

        if cmd == "INSERT":
            bst.insert(int(parts[1]))
        elif cmd == "DELETE":
            bst.delete(int(parts[1]))
        elif cmd == "SEARCH":
            print("FOUND" if bst.search(int(parts[1])) else "NOT FOUND")
        elif cmd == "KTH":
            print(bst.kth(int(parts[1])))
        elif cmd == "RANGE":
            a, b = int(parts[1]), int(parts[2])
            vals = bst.range(a, b)
            print(" ".join(map(str, vals)))
        elif cmd == "LCA":
            a, b = int(parts[1]), int(parts[2])
            ans = bst.lca(a, b)
            print(ans if ans is not None else "NONE")
        elif cmd == "PREDECESSOR":
            ans = bst.predecessor(int(parts[1]))
            print(ans if ans is not None else "NONE")
        elif cmd == "SUCCESSOR":
            ans = bst.successor(int(parts[1]))
            print(ans if ans is not None else "NONE")
        elif cmd == "IS_VALID":
            print("VALID" if bst.is_valid() else "INVALID")
        elif cmd == "HEIGHT":
            print(bst.height())
        elif cmd == "BALANCE_REPORT":
            bst.balance_report()


if __name__ == "__main__":
    main()