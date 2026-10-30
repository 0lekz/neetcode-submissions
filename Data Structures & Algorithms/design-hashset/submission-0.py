class MyHashSet:

    def __init__(self):
        self.keys = []

    def add(self, key: int) -> None:
        if (not(self.contains(key))):
            self.keys.append(key)
        else:
            return

    def remove(self, key: int) -> None:
        if (self.contains(key)):
            # remove key
            for i in range(len(self.keys)):
                if self.keys[i] == key:
                    del self.keys[i]
                    return
        else:
            return

    def contains(self, key: int) -> bool:
        for k in self.keys:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)