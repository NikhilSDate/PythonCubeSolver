class ListWrapper:
    def __init__(self, array):
        self.array = array

    def __eq__(self, other):
        return self.array == other.array

    def __hash__(self):
        result=0
        for element in self.array:
            result = 31*result+element
        return result
