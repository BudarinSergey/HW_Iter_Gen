nested_list = [
        [['a'], ['b'], 'c'],
        [[[['d']]], 'e', 'f', [['h']], False],
        [1, [[[2]]], None]
]



class FlatIteratorAdv:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.iterators_queue = []
        self.current_iterator = iter(self.multi_list)
        return self

    def __next__(self):
        while True:
            try:
                self.current_element = next(self.current_iterator)
            except StopIteration:
                if not self.iterators_queue:
                    raise StopIteration
                else:
                    self.current_iterator = self.iterators_queue.pop()
                    continue
            if isinstance(self.current_element, list):
                self.iterators_queue.append(self.current_iterator)
                self.current_iterator = iter(self.current_element)
            else:
                return self.current_element

for item in FlatIteratorAdv(nested_list):
    print(item)


print('-----------Generator-----------')

def flat_generatorAdv(multi_list):
    for elem in multi_list:
        if isinstance(elem, list):
            for sub_elem in flat_generatorAdv(elem):
                yield sub_elem
        else:
            yield elem


for item in flat_generatorAdv(nested_list):
        print(item)