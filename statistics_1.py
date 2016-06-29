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
ax1 = plt.subplot2grid((2,1),(0,0))
#not required before std part 2
ax2 = plt.subplot2grid((2,1),(1,0), sharex = ax1)


HPI_data = pd.read_pickle('fiddy_states3.pickle')


HPI_data['TX12MA'] = pd.rolling_mean(HPI_data['TX'], 12)
HPI_data['TX12STD'] = pd.rolling_std(HPI_data['TX'], 12)

print HPI_data[['TX', 'TX12MA', 'TX12STD']].head()


'''
HPI_data.dropna(inplace = True)
'''
'''
HPI_data[['TX', 'TX12MA', 'TX12STD']].plot(ax = ax1)
'''
#these 2 lines required after std part 2


HPI_data[['TX', 'TX12MA' ]].plot(ax = ax1)
HPI_data[[ 'TX12STD']].plot(ax = ax2)


plt.legend(loc = 4)
plt.show()
