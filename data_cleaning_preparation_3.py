# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 16:42:35 2023

@author: sriva
"""
import os

os.chdir('C:\\Users\\sriva\\Downloads\\Data_Science\\ML_Projects\\AQI_prediction')


#Taking only the data from 2013-2016, rest all can be used as validation set
from extracting_plot_output_2 import avg_data_2013, avg_data_2014, avg_data_2015, avg_data_2016, avg_data_2017, avg_data_2018
#lst=avg_data_2013() #list that contains all the per day average values of PM2.5 (output feature) of 2013 year

## now we have to extract all the input features from the tables of each html pages that we extracted in the 1st process
import requests
import sys
import pandas as pd
from bs4 import BeautifulSoup #for webscraping from html pages
import os
import csv

def met_data(month, year): #meta data
    
    file_html = open('Data/Html_Data/{}/{}.html'.format(year,month), 'rb') #Data folder ---> year ---> month number.html, read byte mode
    plain_text = file_html.read() #all the content present in the html file will be stored in this variable (para tag, table tag, or any kind of tag)

    tempD = []  #temp data
    finalD = [] #final data

    soup = BeautifulSoup(plain_text, "lxml")    #initializing BeautifulSoup, and "lxml" mode = it is generally used for web scraping
    for table in soup.findAll('table', {'class': 'medias mensuales numspan'}):  #we have extract the table from our html page therefore "table" tag, and then "class"= class of the table in inspection mode. for safe side we are taking a for loop (just in case if we will get multiple tables in the same html page)
        for tbody in table: #inside the inspection section, there is "tbody", which contains all the features present inside the table
            for tr in tbody:    #tr = table rows, i.e extracting every row wise data one by one after iterating through the tbody
                a = tr.get_text()   #extracting each text i.e inside "tr" we have "th" and inde that "th", whatever text (feature name) is present, that needs to be extracted
                tempD.append(a) #appending every data (row-wise) to temporary data

    rows = len(tempD) / 15  #no. of features=15, therefore to get the the no. of rows, we are dividing the collected data by 15

    for times in range(round(rows)):    #iterating through each and every row and then
        newtempD = []
        for i in range(15):  #iterating through all the features, and extracting the data one by one and appending it to our final list
            newtempD.append(tempD[0])
            tempD.pop(0)    #after adding the new data to our finalD, we will remove it from tempD
        finalD.append(newtempD) #run till this line by replacing year=2013 and month = 1 and check the variables in order to undertand better

    length = len(finalD)    #length of finalD, in order to iterate over it

    finalD.pop(length - 1)  #to drop the first (names of features/ column names) and last record/row from every table (list and first row contains unnecessary data= monthly means and totals)
    finalD.pop(0)

    for a in range(len(finalD)):     #dropping unnecessary features (whole columns) (contains mostly missing values)
        finalD[a].pop(6)
        finalD[a].pop(13)
        finalD[a].pop(12)
        finalD[a].pop(11)
        finalD[a].pop(10)
        finalD[a].pop(9)
        finalD[a].pop(0)

    return finalD

#function to combine each and every year's data
def data_combine(year, cs):
    for a in pd.read_csv('Data/Real-Data/real_' + str(year) + '.csv', chunksize=cs):
        df = pd.DataFrame(data=a)
        mylist = df.values.tolist()
    return mylist


##data cleaning and preparing final_data with input and output features together in one file
if __name__ == "__main__":
    if not os.path.exists("Data/Real-Data"):
        os.makedirs("Data/Real-Data")
    for year in range(2013, 2019):
        final_data = []
        with open('Data/Real-Data/real_' + str(year) + '.csv', 'w') as csvfile:
            wr = csv.writer(csvfile, dialect='excel')   #dialect= excel means styling of the sheet will be like excel sheet, but the data will be stored as csv format only.
            wr.writerow(
                ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        for month in range(1, 13):
            temp = met_data(month, year)    #we will get our data successfully here
            final_data = final_data + temp  #we will append our working/useful data to our final data
            
        pm = getattr(sys.modules[__name__], 'avg_data_{}'.format(year))()   #calling each avg_data_year functions that are imported in first line in a variable

        if len(pm) == 364:
            pm.insert(364, '-')

        for i in range(len(final_data)-1):   #appending the above pm values (stored in "pm" variable), and appending it at the last column of our final_data
            # final[i].insert(0, i + 1)
            final_data[i].insert(8, pm[i])

        with open('Data/Real-Data/real_' + str(year) + '.csv', 'a') as csvfile:  #create a Real-Data folder and store those values of rows which does not have any blank value="", or "-" values, i.e. we will raise flag=1 to such values and if the flag=1 then we will not write the rows value
            wr = csv.writer(csvfile, dialect='excel')   
            for row in final_data:
                flag = 0
                for elem in row:
                    if elem == "" or elem == "-":
                        flag = 1
                if flag != 1:
                    wr.writerow(row)
                    
    data_2013 = data_combine(2013, 600) #chunksize=600, just in case if ram is smaller and it is not necessary to be = 600
    data_2014 = data_combine(2014, 600)
    data_2015 = data_combine(2015, 600)
    data_2016 = data_combine(2016, 600)
    data_2017 = data_combine(2017, 600) 
    data_2018 = data_combine(2018, 600)
    
    total=data_2013+data_2014+data_2015+data_2016 #combining the 2013,2014,2015,2016 data
    
    with open('Data/Real-Data/Real_Combine.csv', 'w') as csvfile:
        wr = csv.writer(csvfile, dialect='excel')
        wr.writerow(
            ['T', 'TM', 'Tm', 'SLP', 'H', 'VV', 'V', 'VM', 'PM 2.5'])
        wr.writerows(total)
        
        
df=pd.read_csv('Data/Real-Data/Real_Combine.csv')   #now check df variable for the final data