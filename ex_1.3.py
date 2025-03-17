class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None

    # Método de inserção
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    # Método de busca
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        # Caso base: nó é None ou o valor foi encontrado
        if node is None:
            return False
        
        if node.value == key:
            return True
        
        # Se o valor a ser buscado for menor, vai para a subárvore esquerda
        if key < node.value:
            return self._search_recursive(node.left, key)
        
        # Se o valor a ser buscado for maior, vai para a subárvore direita
        return self._search_recursive(node.right, key)

    # Percurso In-order
    def inorder(self):
        elements = []
        self._inorder_recursive(self.root, elements)
        return elements

    def _inorder_recursive(self, node, elements):
        if node:
            self._inorder_recursive(node.left, elements)
            elements.append(node.value)
            self._inorder_recursive(node.right, elements)

    # Percurso Pre-order
    def preorder(self):
        elements = []
        self._preorder_recursive(self.root, elements)
        return elements

    def _preorder_recursive(self, node, elements):
        if node:
            elements.append(node.value)
            self._preorder_recursive(node.left, elements)
            self._preorder_recursive(node.right, elements)

    # Percurso Post-order
    def postorder(self):
        elements = []
        self._postorder_recursive(self.root, elements)
        return elements

    def _postorder_recursive(self, node, elements):
        if node:
            self._postorder_recursive(node.left, elements)
            self._postorder_recursive(node.right, elements)
            elements.append(node.value)


# Testando a implementação
bst = BST()
elements = [50, 30, 70, 20, 40, 60, 80]
for elem in elements:
    bst.insert(elem)

# Testando a busca de um valor
search_value = 40
found = bst.search(search_value)

if found:
    print(f"O valor {search_value} foi encontrado na árvore.")
else:
    print(f"O valor {search_value} não foi encontrado na árvore.")
