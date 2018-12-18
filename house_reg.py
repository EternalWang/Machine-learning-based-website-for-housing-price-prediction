# -*- coding: utf-8 -*-

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn import tree
from sklearn import metrics
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
class HouseReg:
    def __init__(self):  
        train = pd.read_csv('housetrain.csv', encoding='gbk')
        test = pd.read_csv('housetest.csv', encoding='gbk')
        
        #LogisticRegression
        x_cols = list(train.columns[1:].values)
        scaler = preprocessing.StandardScaler().fit(train[x_cols])
        scaler2= preprocessing.StandardScaler().fit(train['totalPrice'].values.reshape(-1,1))
        self.sc1=scaler
        self.sc=scaler2
        
        self.reg=RandomForestRegressor(n_estimators=100)
        self.reg.fit(scaler.transform(train[x_cols]),
                     np.ravel(scaler2.transform( train['totalPrice'].values.reshape(-1,1))))

        
        pred=self.reg.predict(scaler.transform(test[x_cols]))
        
        mse=metrics.mean_squared_error(test['totalPrice'],self.sc.inverse_transform(pred))
        print('MSE:'+str(mse))
    
    def result(self,arg):
        res=self.reg.predict(self.sc1.transform([arg]))
        res=self.sc.inverse_transform(res)
        return res[0]
    
if __name__=='__main__':
    reg=HouseReg()