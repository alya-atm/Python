import pandas as pd

import xgboost as xgb

def model_xgb(clear):
    ex=clear[0]
    ex['week_of_year'] = ex.date.dt.weekofyear
    dummiesH=pd.get_dummies(ex['week_of_year'])
    ex = pd.concat([ex, dummiesH], axis=1)
    ex['price'] = ex['rev_bonus_m']
    ex['bonus'] = ex['rev_m']
    ex['sales_lag12week'] = ex['sales_without_outliers'].shift(12)
    ex['sales_lag52week'] = ex['sales_without_outliers'].shift(52)
    y = ex['sales_without_outliers']
    x = ex[['23 февраля', '8 марта','День победы','Новый Год','Рождество', 'День перед Новым годом', 'День перед 8 марта', 'shots','day15','price','bonus', 'sales_lag12week',
    'sales_lag52week', 1, 2, 3, 4, 5, 6,7, 8, 9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]]
    test_size = 12
    y_train = y[: -test_size]
    y_test = y[-test_size:]
    x_train = x[: -test_size]
    x_test = x[-test_size:]
    model = xgb.XGBRegressor(max_depth=4, base_score=ex['sales_without_outliers'].mean(), learning_rate=0.74,
                     reg_lambda=0.76, n_estimators=100,
                     eval_metric='rmse', min_child_weight=1, gamma=0, reg_alpha=0.82, subsample=1,
                     early_stopping_rounds=10,
                     seed=52)
    model.fit(x_train, y_train)
    XB_test = model.predict(x_test)
    XB_test =list(map(lambda x: 0 if x < 0 else x, XB_test))
    return ex,XB_test,y_test