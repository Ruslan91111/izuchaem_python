"""d"""

# Создаем хеш-таблицу с тремя хеш-таблицами внутри.
graph = {}

graph['start'] = {}
# Соседи от начала: a со стоимостью 6 и b со стоимостью 2
graph['start']['a'] = 6
graph['start']['b'] = 2
# Включаем в граф остальные узлы и их соседей.
graph['a'] = {}
graph['a']['fin'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5
# Конечный узел без соседей.
graph['fin'] = {}


# хеш-таблица для хранения стоимости всех узлов.
# Представление бесконечности в Питоне.
infinity = float("inf")
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity


# Хеш - таблица для родителей.
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['in'] = 'None'

# Список - массив для отработанных узлов.
processed = []


# Параметром принимает словарь costs
def find_lowest_cost_node(costs):
    # Меньшая стоимость бесконечна.
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Перебрать все значения в словаре costs по ключу.
    for node in costs:
        cost = costs[node]
        # Если значение меньше минимального и этот узел еще не был обработан.
        if cost < lowest_cost and node not in processed:
            # Он назначается новым узлом с наименьшей стоимостью.
            # Значение
            lowest_cost = cost
            # Ключ
            lowest_cost_node = node
    # Вернуть самый дешевый узел.
    return lowest_cost_node


# Найти узел с наименьшей стоимостью среди необработанных
node = find_lowest_cost_node(costs)
# Пока не все узлы обработаны.
while node is not None:
    cost = costs[node]
    neigbors = graph[node]
    for n in neigbors.keys():
        new_cost = cost + neigbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


print(costs)





