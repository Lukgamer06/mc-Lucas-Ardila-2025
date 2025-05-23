class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BTree:
    def __init__(self, m):
        self.root = BTreeNode(True)
        self.m = m  # orden del árbol
    
    def insert(self, key):
        root = self.root
        if len(root.keys) == (2 * self.m) - 1:
            new_root = BTreeNode()
            new_root.children.append(root)
            self._split_child(new_root, 0)
            self.root = new_root
            self._insert_non_full(new_root, key)
        else:
            self._insert_non_full(root, key)
    
    def _insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.m) - 1:
                self._split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)
    
    def _split_child(self, parent, index):
        m = self.m
        child = parent.children[index]
        new_node = BTreeNode(child.leaf)
        
        parent.keys.insert(index, child.keys[m - 1])
        parent.children.insert(index + 1, new_node)
        
        new_node.keys = child.keys[m:(2 * m) - 1]
        child.keys = child.keys[0:m - 1]
        
        if not child.leaf:
            new_node.children = child.children[m:(2 * m)]
            child.children = child.children[0:m]
    
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root
        print(f"Nivel {level}: {node.keys}")
        if not node.leaf:
            for child in node.children:
                self.print_tree(child, level + 1)

# Crear árbol B con m=5
btree = BTree(5)
elements = [22,15,1,12,4,20,13,30,18,5,6,29,11,27,7,28,10,14,21,2,19,3]

# Insertar elementos en orden para mejor visualización
for num in sorted(elements):
    btree.insert(num)

print("Árbol B (m=5):")
btree.print_tree()