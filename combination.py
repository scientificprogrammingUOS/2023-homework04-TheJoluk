import numpy as np 

# implement your function to combine two numpy arrays 

def combination(a, b, axis = 0):
    a = a.squeeze()
    b = b.squeeze()
    combination = np.concatenate((a, b), axis)
    return combination


if __name__ == "__main__":
    # use this for your own testing!

    pass
