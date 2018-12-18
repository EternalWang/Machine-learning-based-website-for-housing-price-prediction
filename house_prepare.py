# -*- coding: utf-8 -*-

import pandas as pd 

df = pd.read_csv('new.csv', encoding='gbk')
df = df[df['tradeTime']>'2015-12-31']  # 只使用2016年之后的数据
df = df.drop(['ladderRatio','price','url', 'id', 'Cid', 'tradeTime', 'DOM','followers','district','communityAverage'], axis = 1)
df = df.dropna(axis = 0)
# floor 高 中 低 底 顶
floor_mapping = {'高':0, '中':1,'低':2, '底':3,'顶':4, '未知':5}
df['floor'] = df['floor'].str.split(' ',expand=True)[0]
df['floor'] = df['floor'].map(floor_mapping)

df.loc[df['constructionTime']=='未知','constructionTime']=2000 # 平均数

total=df['totalPrice']
df.drop(labels=['totalPrice'],axis=1,inplace = True)
df.insert(0,'totalPrice',total)

df = df.sample(frac=1.0)  # 全部打乱
cut_idx = int(round(0.1 * df.shape[0]))
df_test, df_train = df.iloc[:cut_idx], df.iloc[cut_idx:] #取测试集和训练集

df_test.to_csv('housetest.csv',index=False)
df_train.to_csv('housetrain.csv',index=False)

