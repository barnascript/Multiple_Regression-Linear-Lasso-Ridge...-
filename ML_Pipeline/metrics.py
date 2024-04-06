import numpy as np  

def mean_squared_error(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)

# y_true = [1, 2, 3, 4]
# y_pred = [0,1, 2, 3]

# err = y_true - y_pred = [1, 1, 1, 1]

# err**2 = [1, 1, 1, 1]

# mean = 1+1+1+1/4 = 1 --mean_squared_error


def r2_score(y_true, y_pred):
    corr_matrix = np.corrcoef(y_true, y_pred)
    corr = corr_matrix[0, 1]
    return corr ** 2