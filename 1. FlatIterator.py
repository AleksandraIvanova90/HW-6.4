
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


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()