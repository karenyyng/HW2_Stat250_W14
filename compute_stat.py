#!/usr/bin/env python
#----------------------------------------------------------------------
# Author: Karen Ng <karenyng@ucdavis.edu>
# trying to parallelize the code
# PEP8 compliant
#----------------------------------------------------------------------
import pandas as pd
import numpy as np

data_path = "./data/"

# First read in the data from 1987 to 2007
year = [data_path + str(i) + ".csv" for i in range(1987, 2008)]
# create empty dataframe
delay1 = pd.DataFrame()
# loop through the year-by-year csvs
for yr_file in year:
    # read in relevant column from csv file using pandas
    temp = pd.read_csv(yr_file, usecols=["ArrDelay"])
    # append the dataframes - this is done by reference not by value
    delay1 = delay1.append(temp)
    print 'appending ' + yr_file + ' - total lines = ' + \
        '{0}'.format(delay1.shape[0])

# create another empty dataframe for handling month by month csv
delay2 = pd.DataFrame()
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
year = [data_path + str(i) + "_" +
        mth + ".csv" for i in range(2008, 2013) for mth in month]
# loop through all the month-by-month csv
for yr_file in year:
    # tell pandas to read only the relevant column in the csv
    temp = pd.read_csv(yr_file, usecols=["ARR_DELAY"])
    # append them to the dataframe by reference
    delay2 = delay2.append(temp)
    print 'appending ' + yr_file + ' - total lines = ' + \
        '{0}'.format(delay2.shape[0] + delay1.shape[0])

# hackish way to remove the column name of the dataframe to append
# the two types of csv columns together
# so I can compute the statistics in one pass later on
delay1 = np.array(delay1)
delay2 = np.array(delay2)
delay = np.append(delay1, delay2)
delay = pd.DataFrame(delay)
print 'total number of valid lines = {0}'.format(delay.dropna().shape[0])

# note that pandas ignores nans automatically while computing stats
print 'saving to results2.txt'
f = open('results2.txt', 'w')
f.write('mean = {0}\n'.format(delay[0].mean()))
f.write('median = {0}\n'.format(delay[0].median()))
f.write('std = {0}\n'.format(delay[0].std()))
f.close()
