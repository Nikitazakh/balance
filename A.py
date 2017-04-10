class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data) #создание вершины
        if self.root is None: #формирование колрня
            self.root = node
            return
        p = self.root
        while True: #формирование ветвей
            if data < p.data:
                if p.left is None:
                    p.left = node
                    return
                else:
                    p = p.left
            else:
                if p.right is None:
                    p.right = node
                    return
                else:
                    p = p.right

    def norm_print(self, p, res):
        if p is None:
            return
        self.norm_print(p.left, res)
        res.append(p.data)
        self.norm_print(p.right, res)

    def print(self):
        p = self.root
        res = []
        self.norm_print(p, res)
        print(*res)

tree = Tree()
for x in [7, 3, 2, 1, 9, 5, 4, 6, 8]:
    tree.add(x)
tree.print()  # напечатает 1 2 3 4 5 6 7 8 9