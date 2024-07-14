def pack_backpack(items, weights, max_capacity):
    backpack = []
    total_weight = 0
    for item, weight in zip(items, weights):
        if total_weight + weight <= max_capacity:
            backpack.append(item)
            total_weight += weight
    return backpack


items = ['Вода', 'Одежда', 'Лекарства', 'Еда', 'Розжиг', 'Компас', 'Спальный мешок']
weights = [3, 5, 2, 4, 2, 1, 4]
max_capacity = 15
result = pack_backpack(items, weights, max_capacity)
print(result)
