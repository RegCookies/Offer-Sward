def Find(self, target, array):
    if array == [[]]:
        return False
    for i in range(len(array)):
        if array[i][0] > target:
            continue
        else:
            for j in range(len(array[i])):
                if array[i][j] == target:
                    return True
    return False
