# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 10:31:55 2021

@author: wyuan
"""

import os
import pandas as pd

# Merge FN_Fn046 data
os.chdir('FN_Fn046/')
fn046frame = []
for file in os.listdir():
    if file.endswith('.csv'):
        data = pd.read_csv(file)
        fn046frame.append(data)
    else:
        continue
df_fn046 = pd.concat(fn046frame).sort_values(by=['Stkcd','Accper'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
os.chdir('../')
df_fn046.to_csv('FN_Fn046.csv', index=False, encoding='utf_8_sig')

# Merge TRD_Dalyr data
os.chdir('TRD_Dalyr/')
dalyrframe = []
for folder in os.listdir():
    os.chdir(folder + '/')
    for file in os.listdir():
        if file.endswith('.csv'):
            data = pd.read_csv(file)
            dalyrframe.append(data)
        else:
            continue
    os.chdir('../')
df_dalyr = pd.concat(dalyrframe).sort_values(by=['Stkcd','Trddt'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
os.chdir('../')
df_dalyr.to_csv('TRD_Dalyr.csv', index=False, encoding='utf_8_sig')

# Merge TRD_Week data
os.chdir('TRD_Week/')
weekframe = []
for file in os.listdir():
    if file.endswith('.csv'):
        data = pd.read_csv(file)
        weekframe.append(data)
    else:
        continue
df_week = pd.concat(weekframe).sort_values(by=['Stkcd', 'Trdwnt'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
os.chdir('../')
df_week.to_csv('TRD_Week.csv', index=False, encoding='utf_8_sig')

# # Merge HLD_Negshr data
# os.chdir('HLD_Negshr/')
# negshrframe = []
# for folder in os.listdir():
#     os.chdir(folder + '/')
#     for file in os.listdir():
#         if file.endswith('.csv'):
#             data = pd.read_csv(file)
#             negshrframe.append(data)
#         else:
#             continue
#     os.chdir('../')
# df_negshr = pd.concat(negshrframe).sort_values(by=['Stkcd','Reptdt'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
# os.chdir('../')
# df_negshr.to_csv('HLD_Negshr.csv', index=False, encoding='utf_8_sig')

# Merge HLD_Shareholders data
os.chdir('HLD_Shareholders/')
shareholdersframe = []
for file in os.listdir():
    if file.endswith('.csv'):
        data = pd.read_csv(file)
        shareholdersframe.append(data)
    else:
        continue
df_shareholders = pd.concat(shareholdersframe).sort_values(by=['Stkcd', 'Reptdt'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
os.chdir('../')
df_shareholders.to_csv('HLD_Shareholders.csv', index=False, encoding='utf_8_sig')

# # Merge HLD_Negshr data
# os.chdir('HLD_Negshr/')
# negshrframe = []
# for file in os.listdir():
#     if file.endswith('.csv'):
#         data = pd.read_csv(file, error_bad_lines=False)
#         negshrframe.append(data)
#     else:
#         continue
# df_negshr = pd.concat(negshrframe).sort_values(by=['Stkcd', 'Reptdt'], ascending=(True, True)).reset_index().drop(['index'], axis=1)
# os.chdir('../')
# df_negshr.to_csv('HLD_Negshr.csv', index=False, encoding='utf_8_sig')
