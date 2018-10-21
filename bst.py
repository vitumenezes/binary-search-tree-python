#Implementation of individual node of tree
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.data = key


#inserts a value into tree
def insert(root, node):
    if root is None:
        root = node;
    else:
        if root.data < node.data:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
                if root.left is None:
                    root.left = node
                else:
                    insert(root.left, node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=' ')
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
    index_cont = 1

    while(not done):
        if index_cont == index:
            current = s.pop()
            return current.data
            break

        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s) >0 ):
                current = s.pop()
                current = current.right
            else:
                done = 1

        index_cont += 1


if __name__ == "__main__":
    root = Node(10)

    insert(root, Node(20))
    insert(root, Node(30))
    insert(root, Node(40))
    insert(root, Node(50))
    insert(root, Node(2))
    insert(root, Node(3))
    insert(root, Node(5))
    insert(root, Node(4))

    print(search(root, 3))
    print(search(root, 4))
    print(search(root, 1))

    print(enesimo_elemento(root, 4))
    inorder(root)
