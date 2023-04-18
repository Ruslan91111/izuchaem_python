"""Задается бинарное дерево, состоящее из узлов - задача вывести значения в дереве в списке,
значения должны быть расположены сверху вниз, слева направо. Если не передано ни одного узла вернуть пустой список."""


# Класс задает узел дерева.
class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(node):
    result_list = []
    # Очередь из узлов - список, который мы будем наполнять узлами в цикле.
    queue_of_nods = [node]

    # Пока очередь узлов не пуста.
    while queue_of_nods:
        # Берем первый элемент в очереди, автоматически он удаляется из очереди.
        first_in_queue = queue_of_nods.pop(0)
        # Если элемент в очереди не None, а значение.
        if first_in_queue is not None:
            # Добавляем значение в резулютирующий список.
            result_list.append(first_in_queue.value)
            # В очередь узлов закидываем левый и правый узлы.
            queue_of_nods += [first_in_queue.left, first_in_queue.right]

    if node:
        return result_list
    # Если не передано ни одного узла вернуть пустой список.
    return []

print((tree_by_levels(None)))
print(tree_by_levels((Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1))))

# [1, 2, 3, 4, 5, 6]
# (Node(
#     Node(
#         None,
#         Node(
#             None, None, 4),
#         2),
#     Node(
#         Node(
#             None, None, 5),
#         Node(
#             None, None, 6),
#         3),
#     1
# )
# )
