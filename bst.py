#Implementation of individual node of tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key
        self.left_nodes = 0
        self.right_nodes = 0
        self.parent = None


#inserts a value into tree
def insert(root, node):
    if root.data < node.data:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)
        root.right_nodes += 1
    else:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
        root.left_nodes += 1


#in order traversal
#prints all values
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


#search a value in the tree
def search(root, value):
    if root is None:
        return False

    if root.data == value:
        return True

    if root.data < value:
        return search(root.right, value)

    return search(root.left, value)


#returns a node at the index informed
def enesimo_elemento(root, index):
    current = root
    s = []
    done = 0
    aux = None

    while not done and index > 0:

        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s) > 0):
                index -= 1
                aux = s.pop()
                current = aux.right
            else:
                done = 1

    return aux.data


#returns the index of value informed
def posicao(root, value):
    current = root
    s = []
    done = 0
    index = 1

    while not done:
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s) > 0):
                current = s.pop()

                if current.data == value:
                    return index

                index += 1
                current = current.right
            else:
                done = 1


def nodes_count(root):
    pass


#no comments at all
def mediana(root):
    pass

if __name__ == "__main__":
    root = Node(10)

    insert(root, Node(30))
    insert(root, Node(20))
    insert(root, Node(40))
    insert(root, Node(19))
    insert(root, Node(21))
    insert(root, Node(39))
    insert(root, Node(41))
    insert(root, Node(6))
    insert(root, Node(4))
    insert(root, Node(8))
    insert(root, Node(7))
    insert(root, Node(9))
    insert(root, Node(3))
    # insert(root, Node(5))

    # print(search(root, 3))
    # print(search(root, 4))
    # print(search(root, 1))

    inorder(root)
    print(enesimo_elemento(root, 3))
    print(posicao(root, 4))
    print(root.right_nodes)
