import sys

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
        print(f'>>> ERRO: O valor {node.data} não pôde ser adicionado pois já existe na árvore.')
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


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)


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
    size = root.left_nodes + root.right_nodes + 1

    if not root or n <= 0 or n > size:
        return None


    if n <= root.left_nodes:
        return enesimo_elemento(root.left, n)

    elif n == root.left_nodes + 1:
        return root

    else:
        return enesimo_elemento(root.right, n - root.left_nodes - 1)


def posicao(root, x):
    current = root
    s = []
    done = 0
    count = 1

    while(not done):
        if current is not None:
            s.append(current)
            current = current.left
        else:
            if(len(s) > 0):
                current = s.pop()
                if current.data == x:
                    return count
                current = current.right
                count += 1
            else:
                done = 1

    return 0


def mediana(root):
    size = root.left_nodes + root.right_nodes + 1
    med = 0
    if size % 2 == 0:
        med = size // 2
    else:
        med = (size // 2) + 1

    return enesimo_elemento(root, med).data


def eh_cheia(root):
    h = get_height(root)
    size = root.left_nodes + root.right_nodes + 1

    return size == ((2 ** h) - 1)


def eh_completa(root):
    h = get_height(root)
    size = root.left_nodes + root.right_nodes + 1

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
    if len(sys.argv) < 3:
        print("Número inválido de argumentos!")
        exit()

    inputs = open(sys.argv[1], "r")

    #checks if the first entry are the values to insert on tree
    string = str(inputs.readline().split(' ')[0])
    if not string.isdigit():
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ERRO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
        print("O primeiro arquivo deve conter os valores a serem inseridos na árvore.\nVerifique a entrada!")
        exit()

    #returns to the beginning of the buffer
    inputs.seek(0)

    #reads all the values
    values = list(map(int, inputs.readline().split(' ')))
    root = Node(values.pop(0))
    nodes = [Node(value) for value in values]

    #inserts all the values on the tree
    inserir(root, nodes)
    print()

    commands = open(sys.argv[2], "r")
    for index, command in enumerate(commands):
        command_, argument = command.replace('\n', ' ').split(' ', 1)
        print(f'============ COMANDO: {command_} - Argumento(s): {argument}=============')

        if command_ == 'ENESIMO':
            no = enesimo_elemento(root, int(argument))
            if no:
                print(f'Elemento na posição {argument} -> {no.data}')
            else:
                print(f'>>> ERRO: A arvore não possui um {argument}° elemento')

        elif command_ == 'POSICAO':
            position = posicao(root, int(argument))

            if position:
                print(f'Posição do elemento {argument} -> {position}')
            else:
                print(f'>>> ERRO: O elemento {int(argument)} não está na árvore.')

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
            flag = insira(root, Node(int(argument)))
            if flag:
                print(f'O valor {argument} foi adicionado!')

        else:
            print('Nenhum comando correspondente encontrado!')

        print('')
