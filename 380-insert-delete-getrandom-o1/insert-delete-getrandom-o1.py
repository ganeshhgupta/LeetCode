import random

class RandomizedSet:

    def __init__(self):
        self.val_to_index = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        
        #swap the val with the last element and pop it
        last = self.nums[-1]
        idx = self.val_to_index[val]
        self.nums[idx] = last
        self.val_to_index[last] = idx
        self.nums.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()