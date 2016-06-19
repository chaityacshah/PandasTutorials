import pandas as pd
#import matplotlib.pyplot as plt
import numpy as np
import quandl
#from matplotlib import style
#style.use('ggplot')

#api key goes here
api_key = ''
#df = quandl.get('FMAC/HPI_AK', authtoken = api_key)
#print df.head()

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

'''
#this is a list:
print fiddy_states

#this is a data frame:
print fiddy_states[0]

#this is a column:
print fiddy_states[0][0]
'''

for abbv in fiddy_states[0][0][1:]:
    print "FMAC/HPI_" + str(abbv)

'''
#this can be useful when user faces some problem with Quandl library
import urllib2
response = urllib2.urlopen('quandl(or any other) link to the dataset that needs to be accessed(read)')
html = response.read()
'''
