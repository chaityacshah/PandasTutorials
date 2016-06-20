import pandas as pd
#import matplotlib.pyplot as plt
#import numpy as np
#import quandl
#from matplotlib import style
#style.use('ggplot')

api_key = ''
#df = quandl.get('FMAC/HPI_AK', authtoken = api_key)
#print df.head()


df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

'''
print pd.merge(df1, df2, on='HPI')

print pd.merge(df1, df2, on=['HPI','Int_rate'])


df1.set_index('HPI', inplace = True)

df3.set_index('HPI', inplace = True)

joined = df1.join(df3)
print joined
'''

merged = pd.merge(df1, df3, on = 'HPI', how = 'left')
merged.set_index('HPI', inplace = True)
print merged
