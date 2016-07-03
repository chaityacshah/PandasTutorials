import pandas as pd
'''
import matplotlib as m
m.use('TkAgg')
import matplotlib.pyplot as plt
'''

#import numpy as np
import quandl
#from matplotlib import style
#style.use('ggplot')
import pickle

api_key = 'KToNAgy-U5cEKsqxcKCN'



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

def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    # print(df.head())
    df = df.resample('1D').mean()
    df = df.resample('M').mean()
    df.columns = ['M30']
    print df.head()
    # print df
    return df
def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df

HPI_data = pd.read_pickle('fiddy_states3.pickle')
m30 = mortgage_30y()
sp500 = sp500_data()
gdp = gdp_data()
HPI_Bench = HPI_Benchmark()
unemployment = us_unemployment()
m30.columns=['M30']
HPI = HPI_Bench.join([m30,sp500,gdp,unemployment])
HPI.dropna(inplace=True)
print(HPI.corr())

#HPI.to_pickle('HPI.pickle')
