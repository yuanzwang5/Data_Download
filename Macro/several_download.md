# Macro Variables Download Descriptions

1. EP, DY, LEV, NI 
- Use all-stocks value-weighted characteristics to calculate;
- Raw data comes from "chars60_raw_no_impute.feather" (Could find on "Dropbox/ResearchData/EquityCharacteristics/")

2. SVAR
- Use daily market return from Fama-French Library, 3 Factors [Daily] (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)
- Use daily market excess return plus risk-free rate to get daily market return (i.e. MKT = MKTRF + RF)
- Use prevailing 12 months' daily return to calculate each month's stock variance;

3. ILL
- Download data directly from https://finance.wharton.upenn.edu/~stambaug/liq_data_1962_2023.txt
- Use column: % Column 2: Levels of aggregated liquidity (Figure 1 in the paper) 

4. INFL
- Download monthly CPI data from https://fred.stlouisfed.org/series/CPIAUCSL
- Then calculate annualized change as annual inflation \
annual inflation = (monthly CPI in this year - monthly CPI in last year) / monthly CPI in last year \
(related same month in each year)

5. TBL, deltatbl
- Download data directly from https://fred.stlouisfed.org/series/TB3MS
- Then calculate deltatbl as the difference between adjacent months \
this month's deltatbl = this month's tbl - last month's tbl

6. DFY
- Download BAA and AAA Corporate Bond Yield data directly from \
--- https://fred.stlouisfed.org/series/BAA \
--- https://fred.stlouisfed.org/series/AAA
- Then calculate the difference between them as Default Yield \
i.e. Default Yield = BAA Corporate Bond Yield - AAA Corporate Bond Yield

7. TMS
- Download Long-Term Government Bond Yields data from https://fred.stlouisfed.org/series/IRLTLT01USM156N
- Then calculate the difference between lty and tbl as Term Spread \
i.e. Term Spread = Long-Term Government Bond Yields - Three Month's Treasury Bill Rate
