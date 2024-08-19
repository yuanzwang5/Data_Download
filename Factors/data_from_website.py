'''
ReadME

This file is used for automatically download factors or test assets data from Fama-French Website

(1) Fama-French Library:
MKTRF, SMB, HML, RMW, CMA, UMD, STR, LTR, NI, BETA, IVOL

(2) Liquidity

'''

import pandas as pd
import os
from pandas.tseries.offsets import *

factor_list = ['MKTRF','SMB','HML','RMW','CMA','RF','UMD','STR','LTR','NI','BETA','IVOL','LIQ']



# FF5
dates_filepath = 'ff5.csv'
ff5 = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip", header=2, index_col=0)
ff5 = ff5.reset_index().loc[:(ff5.index.tolist().index(' Annual Factors: January-December ') - 1)]
ff5 = ff5.rename(columns={'index': 'Date', 'Mkt-RF':'MKTRF'}).set_index('Date')  
ff5 = ff5.astype("float") / 100.0
ff5 = ff5.reset_index()

ff5.to_csv(dates_filepath)


# MOM
dates_filepath = 'mom.csv'
mom = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Momentum_Factor_CSV.zip", header=11, index_col=0)
mom = mom.reset_index().loc[:(mom.index.tolist().index('Annual Factors:') - 1)]
mom = mom.rename(columns={'index': 'Date', 'Mom   ':'UMD'}).set_index('Date')
mom = mom.astype("float") / 100.0
mom = mom.reset_index()

mom.to_csv(dates_filepath)


# STR
dates_filepath = 'st_reversal.csv'
st_reversal = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_ST_Reversal_Factor_CSV.zip", header=11, index_col=0)
st_reversal = st_reversal.reset_index().loc[:(st_reversal.index.tolist().index('Annual Factors:') - 1)]
st_reversal = st_reversal.rename(columns={'index': 'Date','ST_Rev':'STR'}).set_index('Date')
st_reversal = st_reversal.astype("float") / 100.0
st_reversal = st_reversal.reset_index()

st_reversal.to_csv(dates_filepath)


# LTR
dates_filepath = 'lt_reversal.csv'
lt_reversal = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_LT_Reversal_Factor_CSV.zip", header=11, index_col=0)
lt_reversal = lt_reversal.reset_index().loc[:(lt_reversal.index.tolist().index('Annual Factors:') - 1)]
lt_reversal = lt_reversal.rename(columns={'index': 'Date','LT_Rev':'LTR'}).set_index('Date')
lt_reversal = lt_reversal.astype("float") / 100.0
lt_reversal = lt_reversal.reset_index()

lt_reversal.to_csv(dates_filepath)


# NI
dates_filepath = 'ni.csv'
ni = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Portfolios_Formed_on_NI_CSV.zip", header=9, index_col=0)
ni = ni.reset_index().loc[:(ni.index.tolist().index('  Equal Weighted Returns -- Monthly') - 1)]
ni["NI"] = (ni["Lo 10"].astype("float") - ni["Hi 10"].astype("float")) / 100.0
ni = ni[["index", "NI"]]
ni = ni.rename(columns={'index': 'Date'})

ni.to_csv(dates_filepath)


# BETA
dates_filepath = 'beta.csv'
beta = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Portfolios_Formed_on_BETA_CSV.zip", header=9, index_col=0)
beta = beta.reset_index().loc[:(beta.index.tolist().index('  Equal Weighted Returns -- Monthly') - 1)]
beta["BETA"] = (beta["Lo 10"].astype("float") - beta["Hi 10"].astype("float")) / 100.0
beta = beta[["index", "BETA"]]
beta = beta.rename(columns={'index': 'Date'})

beta.to_csv(dates_filepath)


# IVOL
dates_filepath = 'ivol.csv'
ivol = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/Portfolios_Formed_on_RESVAR_CSV.zip", header=9, index_col=0)
ivol = ivol.reset_index().loc[:(ivol.index.tolist().index('  Equal Weighted Returns -- Monthly') - 1)]
ivol["IVOL"] = (ivol["Lo 10"].astype("float") - ivol["Hi 10"].astype("float")) / 100.0
ivol = ivol[["index", "IVOL"]]
ivol = ivol.rename(columns={'index': 'Date'})

ivol.to_csv(dates_filepath)


# Liquidity
dates_filepath = 'liquidity.csv'
liquidity = pd.read_csv("https://finance.wharton.upenn.edu/~stambaug/liq_data_1962_2023.txt", header=10, index_col=0).reset_index()
liquidity = liquidity[liquidity.columns[0]].str.split('\t', expand=True)
liquidity.columns = ['Date', 'Agg Liq.', 'Innov Liq (eq8)', 'LIQ', 'Other']
liquidity = liquidity[liquidity['LIQ'] != '-99'].reset_index(drop=True)
liquidity = liquidity[['Date', 'LIQ']]

liquidity.to_csv(dates_filepath)


##################################################################################################
# All merge together
factors = ff5.merge(mom, on='Date', how='inner').merge(st_reversal, on='Date', how='inner').merge(lt_reversal, on='Date', how='inner').merge(ni, on='Date', how='inner').merge(beta, on='Date', how='inner').merge(ivol, on='Date', how='inner').merge(liquidity, on='Date', how='inner')
factors[factor_list] = factors[factor_list].astype("float")

factors['year'] = factors['Date'].apply(lambda x: str(x)[0:4])
factors['month'] = factors['Date'].apply(lambda x: str(x)[4:6])
factors['day'] = 1
factors['date'] = pd.to_datetime(factors[['year', 'month', 'day']]) + MonthEnd(0)
factors['date'] = factors['date'].apply(lambda x: str(x)[0:10])
factors = factors[['date'] + factor_list]

factors.to_csv('factors_ff_liq.csv', index=False, encoding='utf_8_sig')

