import numpy as np
arr_2d = np.array([[2,1],[4,2]])
print(arr_2d)
new_arr_2d = np.insert(arr_2d,1,[23,32],axis = None)
print(new_arr_2d)   