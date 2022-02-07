#BEGIN

""" Program Begin HERE
Some data Exploration using Python. For PyCharm Edu on the Mac, you may need to install the pandas module.
Assuming that all the needed packages
 are already install for your IDE to find them.
"""
#############################################################
#Program name - Data Exploration
#input - NONE
#output - Some Exploration statistics
###############################################################
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


df = pd.read_csv('/Users/jimvogel/PycharmProjects/MIS581/F.csv')


x = np.array(df['Volume'].tolist()).reshape((-1, 1))
y = np.array(df['Close'].tolist())
model = LinearRegression()
model.fit(x, y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print('Coefficient Of Determination:', r_sq)
print('intercept:', model.intercept_)
print('slope:', model.coef_)
#results = model.fit()
#print results









# Create data_frame of array values
########################################################
# BEGIN extract a 34% sample of data
########################################################
#rows = df.sample(frac =.34)
# validate first to check if sample is 0.25 times data or not
#if (.34*(len(df))== len(rows)):
#    print(len(df), len(rows))

# Display Sample Percentage
#print 'sample of 34%',rows

#END extract a 25% sample of data
############################################################
# BEGIN Split categorical variables by gender, Sum, Mean, count,
# and describe on the data
############################################################

#print x
#print y
#Categorical Variables splitting
#END
