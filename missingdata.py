import pandas as pd
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as plt
#import numpy as np
import quandl
#from matplotlib import style
#style.use('ggplot')
import pickle

api_key = ''
#df = quandl.get('FMAC/HPI_AK', authtoken = api_key)
#print df.head()



def state_list():
    fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiddy_states[0][0][1:]


def grab_initial_state_data():
    states = state_list()

    main_df = pd.DataFrame()

    for abbv in states:
        query = "FMAC/HPI_"+str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df = df.rename(columns = {'Value':abbv})
#        df = df.pct_change()
        df[abbv] = (df[abbv] -df[abbv][0] / df[abbv][0] * 100.0)

#        print df.head()

#        print(query)
        if main_df.empty:
            main_df = df
        else:
#            main_df = pd.merge(main_df, df, right_index=True, left_index=True)
#            main_df = main_df.join(df, lsuffix='_left', rsuffix='_right')
            main_df = main_df.join(df)


    pickle_out = open('fiddy_states3.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()
    print df.head()

def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken = api_key)
    df["Value"] = (df["Value"] -df["Value"][0] / df["Value"][0] * 100.0)
    return df

#grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))


HPI_data = pd.read_pickle('fiddy_states3.pickle')


HPI_data['TX'].plot(ax = ax1)


HPI_data['TX1yr'] = HPI_data['TX'].resample('A', how = 'mean')

print HPI_data[['TX', 'TX1yr']].head()
'''
HPI_data.dropna(how='all', inplace = True)
'''
#HPI_data.fillna(method = 'ffill', inplace = True)

#HPI_data.fillna(method = 'bfill', inplace = True)

#HPI_data.fillna(value = -99999, inplace = True)

HPI_data.fillna(value = -99999, limit = 10, inplace = True)


print HPI_data[['TX', 'TX1yr']].head()

'''
#used to calculate remaining null values
print HPI_data.isnull().values.sum()
'''

HPI_data[['TX', 'TX1yr']].plot(ax = ax1)

plt.legend(loc = 4)
plt.show()
