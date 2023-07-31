
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:54:05 2023

@author: srivastavashantam
"""


## Data Collection - we will use this url - "https://en.tutiempo.net/"
# step 1 - At first, we will collect all the html files that contains data for bangalore city.
# from these url's well can get all the independent features required for this project but they dont contain the output feature i.e. AQI, so we will fetch AQI from a different source.
# output feature is taken from 3rd party api = weathermap.com

# -*- coding: utf-8 -*-

#At first, create a folder with name "Data" inside the working directory, where we will be storing all our fetched data
import os

os.chdir('C:\\Users\\sriva\\Downloads\\Data_Science\\ML_Projects\\AQI-prediction')

import time #in order to compute the execution time
import requests #to download the particular pages in the form of html
import sys

#defining a function to retrieve the information about all the independent features in the form of html pages from 2013 to 2018
def retrieve_html():
    for year in range(2013,2019):#looping for year 2013-2018
        for month in range(1,13):
            if(month<10): #looping for months from jan-september i.e. from month 1-9
                url='http://en.tutiempo.net/climate/0{}-{}/ws-421820.html'.format(month
                                                                          ,year) #this url is dynamically constructed since our year and month will change and new values will take place inside {}. we will be using string formatting in order to replace the first {} with month and the second {} to year
            else: #for months from october-december, i.e. from month 10 - 12 
                url='http://en.tutiempo.net/climate/{}-{}/ws-421820.html'.format(month
                                                                          ,year)
            texts=requests.get(url) #to extract all the information from the url
            text_utf=texts.text.encode('utf=8') #there are some characters that are in the html tag that needs to be fixed therefore utf-8 encoding is used. Now the text_utf variable will be storing all the html files
            
            if not os.path.exists("Data/Html_Data/{}".format(year)): #it will check whether inside the Data folder, a folder named as Html_Data exists or not, and if it does then create subfolders named as year's names and store the info inside it, and if the Html_Data does not exist then create a folder Html_Data inside it and then create subfolders of every year inside it and store all the data
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month),"wb") as output: #open function helps us to open any folder, so we will opening the all the files inside Html_Data folder --> year name--> month name in the write byte mode as our output and write it in .html format inside our folder.
                output.write(text_utf)
            
        sys.stdout.flush() #to flush everything that is being created inside the particular file
 
#we are not using the beautiful soup here but requests.

#main function is the starting point of my execution in python programming language
if __name__=="__main__":
    start_time=time.time() #start time
    retrieve_html()
    stop_time=time.time() #stop time
    print("Time taken {}".format(stop_time-start_time)) #total time of evaluation
        
    
