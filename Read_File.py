__author__ = 's'
import pandas as pd
import numpy as np
from datetime import datetime

def readFile(path):

    df = pd.read_csv(path,sep=';',parse_dates=["Date"],dayfirst=True)
    '''
    df['Date'] = df['Date'].astype(datetime);
    #df['Time'] = df["Time"].astype(datetime.time)
    df=df[df.Voltage != '?']'''
    print df.dtypes
    #print df['Time'][1]
    '''l=len(df.index)
    k=0

    while k<l:
        dt = df['Date'][k]
        dt2 = datetime.strptime(dt,'%d/%m/%Y')
        dt2 = dt2.strftime('%Y/%m/%d')
        df['Date'][k]=dt2
        print df['Date'][k]
        k+=1
    #df['Date']
'''
    '''
    for row in df.iterrows():
        dt=row('Date').astype(datetime.date())
        dt2= datetime.strptime(dt,'%d/%m/%Y')
        dt2 = dt2.strftime('%Y/%m/%d')
        row('Date') = dt2'''
    '''dt= "11/03/2012"
    dt2= datetime.strptime(dt,'%d/%m/%Y')
    print (dt2.strftime('%Y-%m-%d'))'''
    ''' for row in df.iterrows():
        if i<1:
        #if row['Voltage'].astype()=='?':
            #print row[1]['Date']
            i+=1
        else:
            break '''
    df.to_csv("/home/s/Desktop/out2.csv",sep=';')
    #print df['Date'].to_csv('/home/s/Desktop/out2.csv',sep=';'Vo);
    #df.to_csv('/home/s/Desktop/out.csv',sep=';')
    return