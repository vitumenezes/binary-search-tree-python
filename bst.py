class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.left_nodes = 0
        self.right_nodes = 0
        self.parent = None
        self.data = key


def insert(root, node):
    exists = True
    if root.data == node.data:
        print('Duplicated value ' + str(root.data))
        return False
    elif root.data < node.data:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            exists = insert(root.right, node)
        if exists: root.right_nodes += 1
        return exists
    else:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            exists = insert(root.left, node)
        if exists: root.left_nodes += 1
        return exists


def count_node(root):
    if not root:
        return 0

    return 1 + count_node(root.left) + count_node(root.right)


def get_height(node):
    if not node:
        return 0

    if node.left and node.right:
        return 1 + max(get_height(node.left), get_height(node.right))
    elif node.left:
        return 1 + get_height(node.left)
    elif node.right:
        return 1 + get_height(node.right)
    else:
        return 1


def enesimo_elemento(root, n):
    if not root or n <= 0 or n > count_node(root):
        return None

    left_count = 0 if not root.left else count_node(root.left)

    if n <= left_count:
        return enesimo_elemento(root.left, n)

    elif n == left_count + 1:
        return root

    else:
        return enesimo_elemento(root.right, n - left_count - 1)


def posicao(x):
    if not x:
        return None

    index = 0
    cur = x
    prev = None

    while cur:
        if not prev or prev == cur.right:
          index += 1 + (0 if not cur.left else count_node(cur.left))

        prev = cur
        cur = cur.parent

    return index


def mediana(root):
    size = count_node(root)
    if size % 2 == 0:
        size = size / 2
    else:
        size = (size // 2) + 1

    return enesimo_elemento(root, size).data


def eh_cheia(root):
    h = get_height(root)
    size = count_node(root)

    return size == ((2 ** h) - 1)


def eh_completa(root):
    h = get_height(root)
    size = count_node(root)

    return (2 ** (h - 1)) <= size <= ((2 ** h) - 1)


def to_string(root):
    if not root:
        return

    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data, end=' ')
        node = queue.pop(0)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    print("")


if __name__ == "__main__":
    # root = Node(10)
    #
    # node_t = Node(5)
    #
    # insert(root, node_t)
    # insert(root, Node(20))
    # insert(root, Node(11))
    # insert(root, Node(30))
    # insert(root, Node(40))
    # insert(root, Node(4))
    # insert(root, Node(6))

    # print(search(root, 3))
    # print(search(root, 4))
    # print(search(root, 1))

    # print(enesimo_elemento(root, 4))
    # print('----')
    # inorder(root)
    # print('----')
    # print(query(2, root).data)
    # print('----')
    # print(count_node(root))
    # print('----')
    # print(find_by_index(root, 4).data)
    # print('----')
    # size = count_node(root)
    # med = 0
    # if size % 2 == 0:
    #     med = size / 2
    # else:
    #     med = (size // 2) + 1


    # print('------')
    # inorder(root)
    # print_level_order(root)
    # h = get_height(root)
    # print(h)
    # print(size)

    # print((2 ** h) - 1)

    # print((2 ** (h - 1)) <= size <= ((2 ** h) - 1))
    # print(size == ((2 ** h) - 1))

    # print(size)
    # print(find_by_index(root, size).data)
    # print(get_index(node_t))
