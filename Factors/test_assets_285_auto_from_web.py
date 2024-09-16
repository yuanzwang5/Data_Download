# %%
import pandas as pd
import os
from pandas.tseries.offsets import *

# %%
# FF5
ff5 = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_CSV.zip", header=2, index_col=0)
ff5 = ff5.reset_index().loc[:(ff5.index.tolist().index(' Annual Factors: January-December ') - 1)]
ff5 = ff5.rename(columns={'index': 'date', 'Mkt-RF':'MKTRF'}).set_index('date')
ff5 = ff5.astype("float") / 100.0
ff5['lag_MKTRF'] = ff5['MKTRF'].shift(1)
ff5['MKTRF_next'] = ff5['MKTRF'].shift(-1)
ff5 = ff5.reset_index()

# %%
# Size and Book-to-Market ratio
me_bm = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_5x5_CSV.zip", header=9, index_col=0)
me_bm.columns = [f"me{i}_bm{j}" for i in range(1, 6) for j in range(1, 6)]

me_bm = me_bm.reset_index().loc[:(me_bm.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_bm = me_bm.rename(columns={'index': 'date'}).set_index('date')  
me_bm = me_bm.astype("float") / 100.0
me_bm = me_bm.reset_index()
# me_bm

# %%
# Size and Operating Profitability
me_op = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_OP_5x5_CSV.zip", header=15, index_col=0)
me_op.columns = [f"me{i}_op{j}" for i in range(1, 6) for j in range(1, 6)]

me_op = me_op.reset_index().loc[:(me_op.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_op = me_op.rename(columns={'index': 'date'}).set_index('date')  
me_op = me_op.astype("float") / 100.0
me_op = me_op.reset_index()
# me_op

# %%
# Size and Investment
me_inv = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_INV_5x5_CSV.zip", header=10, index_col=0)
me_inv.columns = [f"me{i}_inv{j}" for i in range(1, 6) for j in range(1, 6)]

me_inv = me_inv.reset_index().loc[:(me_inv.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_inv = me_inv.rename(columns={'index': 'date'}).set_index('date')  
me_inv = me_inv.astype("float") / 100.0
me_inv = me_inv.reset_index()
# me_inv

# %%
# Size and Momentum
me_mom = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_Prior_12_2_CSV.zip", header=7, index_col=0)
me_mom.columns = [f"me{i}_mom{j}" for i in range(1, 6) for j in range(1, 6)]

me_mom = me_mom.reset_index().loc[:(me_mom.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_mom = me_mom.rename(columns={'index': 'date'}).set_index('date')  
me_mom = me_mom.astype("float") / 100.0
me_mom = me_mom.reset_index()
# me_mom

# %%
# Size and Market Beta
me_beta = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_BETA_5x5_CSV.zip", header=10, index_col=0)
me_beta.columns = [f"me{i}_beta{j}" for i in range(1, 6) for j in range(1, 6)]

me_beta = me_beta.reset_index().loc[:(me_beta.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_beta = me_beta.rename(columns={'index': 'date'}).set_index('date')  
me_beta = me_beta.astype("float") / 100.0
me_beta = me_beta.reset_index()
# me_beta

# %%
# Size and Short-Term Reversal
me_str = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_Prior_1_0_CSV.zip", header=7, index_col=0)
me_str.columns = [f"me{i}_str{j}" for i in range(1, 6) for j in range(1, 6)]

me_str = me_str.reset_index().loc[:(me_str.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_str = me_str.rename(columns={'index': 'date'}).set_index('date')  
me_str = me_str.astype("float") / 100.0
me_str = me_str.reset_index()
# me_str

# %%
# Size and Long-Term Reversal
me_ltr = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_Prior_60_13_CSV.zip", header=7, index_col=0)
me_ltr.columns = [f"me{i}_ltr{j}" for i in range(1, 6) for j in range(1, 6)]

me_ltr = me_ltr.reset_index().loc[:(me_ltr.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_ltr = me_ltr.rename(columns={'index': 'date'}).set_index('date')  
me_ltr = me_ltr.astype("float") / 100.0
me_ltr = me_ltr.reset_index()
# me_ltr

# %%
# Size and Variance
me_var = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_VAR_5x5_CSV.zip", header=11, index_col=0)
me_var.columns = [f"me{i}_var{j}" for i in range(1, 6) for j in range(1, 6)]

me_var = me_var.reset_index().loc[:(me_var.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_var = me_var.rename(columns={'index': 'date'}).set_index('date')  
me_var = me_var.astype("float") / 100.0
me_var = me_var.reset_index()
# me_var

# %%
# Size and Residual Variance
me_resvar = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_VAR_5x5_CSV.zip", header=11, index_col=0)
me_resvar.columns = [f"me{i}_resvar{j}" for i in range(1, 6) for j in range(1, 6)]

me_resvar = me_resvar.reset_index().loc[:(me_resvar.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_resvar = me_resvar.rename(columns={'index': 'date'}).set_index('date')  
me_resvar = me_resvar.astype("float") / 100.0
me_resvar = me_resvar.reset_index()
# me_resvar

# %%
# Size and Net Share Issues
me_ni = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_NI_5x5_CSV.zip", header=12, index_col=0)
me_ni.columns = [f"me{i}_ni{j}" for i in range(1, 6) for j in range(-1, 6)]

me_ni = me_ni.reset_index().loc[:(me_ni.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_ni = me_ni.rename(columns={'index': 'date'}).set_index('date')  
me_ni = me_ni.astype("float") / 100.0
me_ni = me_ni.reset_index()
# me_ni

# %%
# Size and Accruals
me_ac = pd.read_csv("https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/25_Portfolios_ME_AC_5x5_CSV.zip", header=12, index_col=0)
me_ac.columns = [f"me{i}_ac{j}" for i in range(1, 6) for j in range(1, 6)]

me_ac = me_ac.reset_index().loc[:(me_ac.index.tolist().index('  Average Equal Weighted Returns -- Monthly') - 1)]
me_ac = me_ac.rename(columns={'index': 'date'}).set_index('date')  
me_ac = me_ac.astype("float") / 100.0
me_ac = me_ac.reset_index()
# me_ac

# %%
# Merge together
wait_merge_list = [me_bm, me_op, me_inv, me_mom, me_beta, me_str, me_ltr, me_var, me_resvar, me_ni, me_ac]

df_merge = wait_merge_list[0]

for df in wait_merge_list[1:]:
    df_merge = df_merge.merge(df, on=['date'], how='inner')
print(df_merge.columns.values) # check merge results

df_final = df_merge.melt(id_vars='date', var_name='assets', value_name='ret')
df_final = df_final.merge(ff5[['date','RF','MKTRF','lag_MKTRF','MKTRF_next']], on=['date'], how='inner')
df_final['xret'] = df_final['ret'] - df_final['RF']
df_final['date'] = pd.to_datetime(df_final['date'], format='%Y%m') + MonthEnd(0)
df_final.to_csv('test_assets_285.csv', index=False, encoding='utf_8_sig')
df_final


