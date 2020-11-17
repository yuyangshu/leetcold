class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from random import randrange
        self._list = []
        self._dict = {}
        self._random = randrange

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._dict.keys():
            return False
        else:
            self._list.append(val)
            self._dict[val] = len(self._list) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._dict.keys():
            return False
        else:
            target_index = self._dict[val]
            if len(self._list) > 1 and target_index != len(self._list) - 1:
                self._list[target_index] = self._list[-1]
                self._dict[self._list[-1]] = target_index
            self._dict.pop(val)
            self._list.pop()

            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._list[self._random(len(self._list))]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
