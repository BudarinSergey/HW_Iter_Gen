nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

class FlatIterator:

    def __init__(self, multi_list):
        self.multi_list = multi_list

    def __iter__(self):
        self.list_iter = iter(self.multi_list)
        self.needed_list = []
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1

        if len(self.needed_list) == self.cursor:
            self.needed_list = None
            self.cursor = 0
            while not self.needed_list:
                self.needed_list = next(self.list_iter)
        return self.needed_list[self.cursor]

for item in FlatIterator(nested_list):
    print(item)

print("_______Generator_________")

def flat_generator(nested_list):
  for i in nested_list:
    for z in i:
      yield z


for item in flat_generator(nested_list):
    print(item)