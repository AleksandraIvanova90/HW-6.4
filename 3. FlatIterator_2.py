def get_elements(item):
    stack = [item]
    while stack:
        current = stack.pop()
        if isinstance(current, list) is True and current != []:
            stack.extend(current)
        if isinstance(current, list) is False:
            yield current


class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.index = 0
        self.counter = 0
        self.list_iter = iter([])
        return self

    def get_item(self):
        try:
            item = next(self.list_iter)
            for i in get_elements(item):
                item = i

        except StopIteration:
            item = 'Null'

        return item

    def __next__(self):
        item = self.get_item()
        if item == 'Null':
            self.index += 1
            if self.index > len(self.list_of_list):
                raise StopIteration
            k = self.list_of_list
            list = k[self.index - 1]
            self.list_iter = iter(list)
            item = self.get_item()

        return item


list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

for i in FlatIterator(list_of_lists_2):
    print(i)
