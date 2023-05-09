import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound, upper_bound):
    try:
        int(loc)
        int(scale)
        int(lower_bound)
        int(upper_bound)
    except:
        raise TypeError("Parameter is not a number")

    arr = np.random.normal(loc, scale, 100)
    arr = arr[(arr <= upper_bound) & (arr >= lower_bound)]

    if not lower_bound < upper_bound:
        raise ValueError("lower bound is not smaller than upper bound")

    mean = np.mean(arr)
    std = np.std(arr)

    return (mean, std)


if __name__ == "__main__":
    # use this for your own testing!
    result = gaussian_analysis(1, 1, 0, 2)
    print (result)
    pass
