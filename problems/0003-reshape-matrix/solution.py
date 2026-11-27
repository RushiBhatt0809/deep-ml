import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    x,y = new_shape
    b = np.array(a).flatten()
    if x*y != len(b):
        return []
    reshaped_matrix = b.reshape(x,y).tolist()
    return reshaped_matrix