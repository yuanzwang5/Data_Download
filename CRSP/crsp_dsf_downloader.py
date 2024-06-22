import pandas as pd
import wrds
import pyarrow.feather as feather
import datetime

# Connect to WRDS
conn = wrds.Connection(wrds_username='phd22jm')

# Define the date range for the data download
start_date = datetime.datetime(1970, 1, 1)
end_date = datetime.datetime(2024, 1, 1)
current_date = start_date

# List to store the file names
feather_files = []

while current_date < end_date:
    next_date = current_date + datetime.timedelta(days=365)  # Increment by one year
    if next_date > end_date:
        next_date = end_date

    # SQL query for the current year
    query = f"""
    select a.permno, a.date, a.ret, a.retx, (a.ret - b.rf) as exret, b.mktrf, b.smb, b.hml, a.vol, a.prc, 
           a.shrout, a.askhi, a.bidlo
    from crsp.dsf as a
    left join ff.factors_daily as b
    on a.date=b.date
    where a.date >= '{current_date.strftime('%Y-%m-%d')}'
    and a.date < '{next_date.strftime('%Y-%m-%d')}'
    """

    crsp_chunk = conn.raw_sql(query)
    
    # Save to a Feather file
    file_name = f'crsp_dsf_{current_date.year}_{next_date.year - 1}.feather'
    feather_files.append(file_name)
    with open(file_name, 'wb') as f:
        feather.write_feather(crsp_chunk, f)

    current_date = next_date  # Move to the next interval

# Load all Feather files, concatenate them, and save the final DataFrame
dfs = [feather.read_feather(f) for f in feather_files]
final_df = pd.concat(dfs, ignore_index=True)

# Save the final concatenated DataFrame
final_file_name = 'crsp_dsf_1970_2023_final.feather'
with open(final_file_name, 'wb') as f:
    feather.write_feather(final_df, f)

# Close WRDS connection
conn.close()
