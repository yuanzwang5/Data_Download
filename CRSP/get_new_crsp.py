import pandas as pd
import numpy as np
import datetime as dt
import wrds
from dateutil.relativedelta import *
from pandas.tseries.offsets import *
import pyarrow.feather as feather

conn=wrds.Connection()
crsp = conn.raw_sql("""
                    select *
                    from crsp.msf
                    """)

print(crsp.shape)

with open('crsp_monthly_new.feather','wb') as f:
    feather.write_feather(crsp,f)

crsp = conn.raw_sql("""
                    select *
                    from crsp.dsf
                    """)

print(crsp.shape)

with open('crsp_daily_new.feather','wb') as f:
    feather.write_feather(crsp,f)
