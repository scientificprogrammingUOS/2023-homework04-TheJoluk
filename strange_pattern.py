import numpy as np

# implement the function strange pattern

def strange_pattern(dim):
    arr = np.arange(dim[0] * dim[1]).reshape((dim[0], dim[1]))
    for i in range(dim[1]):
        arr[i] = np.array(range(dim[0])) + (i % 3)
    mask = arr % 3 == 0
    return mask

if __name__ == "__main__":
    # use this for your own testing!
    result = strange_pattern((4, 4))
    print(result.shape)
    print(result)
    pass
