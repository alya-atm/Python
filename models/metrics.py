import numpy as np

from sklearn.metrics import mean_squared_error
#BIAS
def BIAS(y_true, y_pred):
    return np.sum(y_true - y_pred)/np.sum(y_true)*100
#WAPE
def WAPE(y_true, y_pred):
    return (np.sum(np.abs((y_true - y_pred))) /np.sum( y_true)) * 100
#RMSE
def RMSE(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true,  y_pred))
#MAPE
def MAPE(y_true, y_pred):
    return np.mean(np.abs((y_true- y_pred) / y_true)) * 100
