from collections import namedtuple

class SimpleArray(object):
    def __init__(self, mix):
        self.container = [None for i in range(mix)]

    def __len__(self):
        return len(self.container)

    def __setitem__(self, key, value):
        return self.container.__setitem__(key, value)

    def __getitem__(self, item):
        return self.container.__getitem__(item)

    def __delitem__(self, key):
        return self.container.__setitem__(key, None)

    def __str__(self):
        return str(self.container)


class SimpleDict(object):
    Init_length = 8
    Load_factor = 2/3

    def __init__(self):
        self._array_len = SimpleDict.Init_length
        self._array = SimpleArray(self._array_len)
        self._used = 0
        self.dictObj = namedtuple('dictObj', 'key value')

    def __getitem__(self, item):
        key = self._hash(item)
        dictObj = self._array[key]
        if dictObj is not None and dictObj.key == item:
            return dictObj.value
        else:
            for new_key in self._second_hash(key):
                if self._array[new_key] is not None and item == self._array[new_key].key:
                    return self._array[new_key].value

    def __setitem__(self, key, value):
        if (self._used / self._array_len) > SimpleDict.Load_factor:
            self._new_array()

        hash_key = self._hash(key)
        new_key = self._second_hash(hash_key)

        while True:
            if self._array[hash_key] is None or key == self._array[hash_key].key:
                break

            hash_key = next(new_key)

            if abs(hash_key) >= self._array_len:
                self._new_array()
                hash_key = self._hash(key)

        self._array[hash_key] = self.dictObj(key, value)
        self._used += 1

    def __delitem__(self, key):
        hash_key = self._hash(key)
        

