import pandas as pd
import lightgbm as lgb
def model_lgb(clear):
    ex=clear[0]
    ex['week_of_year'] = ex.date.dt.weekofyear
    dummiesH=pd.get_dummies(ex['week_of_year'])
    ex = pd.concat([ex, dummiesH], axis=1)
    ex['sales_lag12week'] = ex['sales_without_outliers'].shift(12)
    ex['sales_lag52week'] = ex['sales_without_outliers'].shift(52)
    ex['price_bonus'] = ex['rev_bonus_m']
    y = ex['sales_without_outliers']
    x = ex[[
    'holiday',
    'shots',
    'day15',
    'day_before_holiday',
    'price_bonus',
    'sales_lag12week',
    'sales_lag52week',
     1, 2, 3, 4,5, 6,7, 8,9, 10,11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
    39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51]]
    test_size = 12
    y_train = y[: -test_size]
    y_test = y[-test_size:]
    x_train = x[: -test_size]
    x_test = x[-test_size:]
    model =lgb.LGBMRegressor(num_leaves=10
                      , max_depth=3, colsample_bytree=0.95, min_child_samples=3, n_estimators=100, learning_rate=0.669,
                      subsample=0.7, seed=52, reg_lambda=0.9,
                      reg_alpha=0, eval_metric='rmse')

    model.fit(x_train, y_train)
    LG_test = model.predict(x_test)
    LG_test =list(map(lambda x: 0 if x < 0 else x, LG_test))
    return ex, LG_test, y_test