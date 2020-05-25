import pandas as pd
import numpy as np
df=pd.read_csv('storesku.csv',parse_dates=['date'])
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
#Убираем товары с длиной ряда <40 недель (чтобы удовлетворялось условие тестовая выборка <0.3*тренировочной)
siz_all=df.groupby(['store','sku']).size().reset_index().sort_values([0])
siz=(siz_all[siz_all[0]>40][['store',"sku"]].drop_duplicates()).reset_index(drop=True)
siz_less=(siz_all[siz_all[0]<41][['store',"sku"]].drop_duplicates()).reset_index(drop=True)
df_less=pd.merge(siz_less,df,how='left',on=['store','sku'])
rank_all=df.groupby(['store','sku']).sum().reset_index().sort_values('sales')
rank=(rank_all[rank_all['sales']>200][['store',"sku"]].drop_duplicates()).reset_index(drop=True)
df=pd.merge(siz,df,how='left',on=['store','sku'])
#Отбираем товары, с низким суммарным показателем продаж
rank_all=df.groupby(['store','sku']).sum().reset_index().sort_values('sales')
#Оставим товары, которые имеют суммарные продажи больше 70 шт
df=pd.merge(rank,df,how='left',on=['store','sku'])
