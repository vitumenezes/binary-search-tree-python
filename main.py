class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.left_nodes = 0
        self.right_nodes = 0
        self.parent = None
        self.data = key


def insira(root, node):
    exists = True
    if root.data == node.data:
        raise(f'Valor duplicado: {root.data}')
        return False
    elif root.data < node.data:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            exists = insira(root.right, node)
        if exists: root.right_nodes += 1
        return exists
    else:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            exists = insira(root.left, node)
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
    med = 0
    if size % 2 == 0:
        med = size // 2
    else:
        med = (size // 2) + 1

    return enesimo_elemento(root, med).data


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


def inserir(root, nodes):
    for node in nodes:
        insira(root, node)


if __name__ == "__main__":
    inputs = open("input.txt", "r")
    values = list(map(int, inputs.readline().split(' ')))
    root = Node(values.pop(0))

    commands = open("commands.txt", "r")
    for index, command in enumerate(commands):
        command_, argument = command.replace('\n', ' ').split(' ', 1)
        print(f'Comando: {command_} - Argumento(s): {argument}')

        nodes = [Node(value) for value in values]
        if index == 0 and command != 'INSIRA':
            inserir(root, nodes)

        if command_ == 'ENESIMO':
            print(f'Elemento na posição {argument} -> {enesimo_elemento(root, int(argument)).data}')

        elif command_ == 'POSICAO':
            node_posicao = [node for node in nodes if node.data == int(argument)]
            print(f'Posição do elemento {argument} -> {posicao(node_posicao[0])}')

        elif command_ == 'MEDIANA':
            print(f'Elemento da posição mediana -> {mediana(root)}')

        elif command_ == 'CHEIA':
            print(f'Árvore é cheia? -> {eh_cheia(root)}')

        elif command_ == 'COMPLETA':
            print(f'Árvore é completa? -> {eh_completa(root)}')

        elif command_ == 'IMPRIMA':
            print('Valores da árvore por níveis:')
            to_string(root)

        elif command_ == 'INSIRA':
            inserir(root, values)
            print('Os valores foram adicionados!')

        else:
            print('Nenhum comando correspondente encontrado!')
