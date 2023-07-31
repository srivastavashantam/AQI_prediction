# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:16:13 2023

@author: sriva
"""
#for output features, from 3rd party api = weathermap.cpm

import pandas as pd
import matplotlib.pyplot as plt
import os

os.chdir('C:\\Users\\sriva\\Downloads\\Data_Science\\ML_Projects\\AQI-prediction')



#we have to find average of PM2.5 for each month of every year from 2013-2018
def avg_data_2013():
    temp_i=0 #temp variable initialized to 0
    average=[] #empty list
    #we have to take the record for every 24 hours (12 hours each in A.M and P.M)
    for rows in pd.read_csv('Data/AQI/aqi2013.csv',chunksize=24): #chunnksize=24 will take 24 records in 1 iteration
        add_var=0  #in order to add each and every hour of data
        avg=0.0 #once we add all the values than we can calculate their average by simply dividing by 12
        data=[] #initializing an empty list
        df=pd.DataFrame(data=rows) #24 rows/records from each iteration are converted into a dataframe first, in order to iterate over them
        for index,row in df.iterrows(): #iterating over 24 rows extracted inside df
            data.append(row['PM2.5']) #appending the PM2.5 values in our empty list 
        for i in data: #now iterating over the collected PM2.5 values that are stored in a list
            if type(i) is float or type(i) is int:  #if PM2.5= float or int value just add them to our initially 0 initialized variable and keep on adding them
                add_var=add_var+i
            elif type(i) is str: #if any string appears in PM2.5 column than checking if there is a mumeric value present as string i.e. ex- "25", then convert these to a float and store them to temp_i variable and keep in adding such numeric strings if any.
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp #add all the values collected 
        avg=add_var/24 #average of PM2.5 per day
        temp_i=temp_i+1 #increment the iteration
        
        average.append(avg) #storing the average of every day in a list
    return average #returing the average value

#### SIMILARY FOR EVERY YEAR #####

def avg_data_2014():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2014.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2015():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2015.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average

    
def avg_data_2016():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2016.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2017():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2017.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    
def avg_data_2018():
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi2018.csv',chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    

#each and every program execution starts from main function
if __name__=="__main__":
    lst2013=avg_data_2013()
    lst2014=avg_data_2014()
    lst2015=avg_data_2015()
    lst2016=avg_data_2016()
    lst2017=avg_data_2017()
    lst2018=avg_data_2018()
    plt.plot(range(0,365),lst2013,label="2013 data")
    plt.plot(range(0,364),lst2014,label="2014 data")
    plt.plot(range(0,365),lst2015,label="2015 data")
    plt.plot(range(0,365),lst2016,label="2016 data")
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()