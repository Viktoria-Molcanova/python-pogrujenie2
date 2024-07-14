
def remove_duplicates(input):
    return list(set([x for x in input if input.count(x) > 1]))


input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print(result)
