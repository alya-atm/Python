# Работа с выбросами с помощью экспоненциального сглаживание

import pandas as pd
def outliers(ex):
    ex['sales1'] = ex['sales_m'].mask((ex['sales_m'] > 0) & ((ex['shots'] > 0) |
                                                             (ex['day15'] > 0)))

    q1 = ex['sales1'].quantile(0.25)
    q3 = ex['sales1'].quantile(0.75)

    outliers_index = ex[(ex['sales1'] < q1) | (ex['sales1'] > q3)]['sales1'].index.values
    series=ex['sales_m']
    alpha=0.1
    result=[series[0]]
    for n in range(1, len(series)):

        result.append(alpha * series[n] + (1 - alpha) * result[n-1])
    result = pd.DataFrame(result, columns=['exp'])
    ex['sales_without_outliers']= ex['sales_m']
    ex.sales_without_outliers.loc[outliers_index]=result.exp.loc[outliers_index]
    res,out = ex,outliers_index
    return res,out