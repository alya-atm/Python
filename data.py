import pandas as pd
import numpy as np
df=pd.read_csv('storesku.xlsx',parse_dates=['date'])
df=df.groupby(['date','store','sku']).sum()
#Пропуски в значениях цен, когда продажи 0
df['sales_m'].fillna(0,inplace=True)
#Обозначение пропусков Nan
df.loc[df['sales_m']==0,['rev_m','bonus_m']]=np.nan
df.loc[(df['sales']==0)&(df['stoсks_mean']==0),'sales_m']=np.nan
#Заменим пропуски с помощью линейной интерполяции (cтолбец цена и бонусы)
df['sales_m'].interpolate(method='linear', inplace=True)
#Заменим пропуски с помощью линейной интерполяции (cтолбец цена и бонусы)
df['rev_m'].interpolate(method='linear', inplace=True)
df['bonus_m'].interpolate(method='linear', inplace=True)
#Замена первых значений в рядах на значение в последующем периоде
df['rev_m'].fillna(method='bfill',inplace=True)
df['bonus_m'].fillna(method='bfill',inplace=True)
df['sales_m'].fillna(method='bfill',inplace=True)
#Пересчитаем цену с учетом бонусов
df['rev_bonus_m']=df['rev_m']-df['bonus_m']
df.reset_index(inplace=True)
ex=df[(df['store']==456)&(df['sku']==3022321)].reset_index(drop=True)
SKU=df['sku'].unique()
STORE=df['store'].unique()
