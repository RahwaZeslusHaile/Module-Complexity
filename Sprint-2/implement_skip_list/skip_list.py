import random


class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * level


class SkipList:
    def __init__(self, max_level=4, p=0.5):
        self.max_level = max_level
        self.p = p
        self.header = Node(None, max_level)
        self.level = 1

    def _random_level(self):
        level = 1
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        update = [None] * self.max_level
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current is None or current.value != value:
            new_level = self._random_level()

            if new_level > self.level:
                for i in range(self.level, new_level):
                    update[i] = self.header
                self.level = new_level

            new_node = Node(value, new_level)

            for i in range(new_level):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def delete(self, value):
        update = [None] * self.max_level
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.value == value:
            for i in range(self.level):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 1 and self.header.forward[self.level - 1] is None:
                self.level -= 1

    def __contains__(self, value):
        current = self.header

        for i in range(self.level - 1, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]

        current = current.forward[0]
        return current is not None and current.value == value

    def to_list(self):
        result = []
        current = self.header.forward[0]

        while current:
            result.append(current.value)
            current = current.forward[0]

        return result