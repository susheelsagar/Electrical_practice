import pandas as pd
import csv
import sys as s
import numpy as np
from datetime import datetime


def readFile(path):

        path2 = '/home/s/Downloads/analyticsvidhya/trainfiles/Internship.csv'
        path3 = '/home/s/Downloads/analyticsvidhya/trainfiles/Student.csv'
        df = pd.read_csv(path,sep=',',parse_dates=["Earliest_Start_Date"],dayfirst=True)
        df2 = pd.read_csv(path2,sep=',',parse_dates=["Internship_deadline","Start_Date"],dayfirst=True)
        indexed_df2 = df2.set_index('Internship_ID')


        df3 = pd.read_csv(path3,sep=',',parse_dates=["Start Date","End Date"],dayfirst=True)
        indexed_df3= df3.set_index('Student_ID')
        f = open('/home/s/Desktop/newtrain.csv', 'wt')
        writer = csv.writer(f)

        '''var = indexed_df2.loc['6653']'''

        '''df4'''
        '''print df.dtypes'''
        '''print '\n'
        print df2.dtypes
        print '\n'
        print df3.dtypes

        l1=len(df.index)
        l2=len(df2.index)
        l3=len(df3.index)
        print l1,l2,l3
        c1=0,c2=0,c3=0'''
        '''internship_row
        student_row'''

        for index, row in df.iterrows():
            intern_id = row['Internship_ID']
            student_id = row['Student_ID']
            internship_row = indexed_df2.loc[[intern_id]]
            student_row = str(indexed_df3.loc[[student_id]])
            '''s1 = pd.Series([row,internship_row,student_row])'''
            data = [internship_row,student_row,row]

            '''columns = ['internship_row','student_row','row']
            df4 = pd.DataFrame(data,index=internship_row, columns=columns)
            df4.to_csv("/home/s/Desktop/out.csv",sep=",")
            break






