### Data Source Descriptions of additional 22 Trading Factors

1. Fama-French (automatically by "data_from_website.py")
- website: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html

- Factors:

    --- (1) MKTRF, SMB, HML, RMW, CMA \
    https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/Data_Library/f-f_5_factors_2x3_archive.html 

    --- (2) UMD, STR, LTR \
        Sorts Involving Prior Returns \
        --> Momentum Factor (Mom) \
        --> Short-Term Reversal Factor (ST Rev) \
        --> Long-Term Reversal Factor (LT Rev)

    --- (3) NI, BETA, IVOL \
        Sorts involving Accruals, Market Beta, Net Share Issues, Daily Variance, and Daily Residual Variance \
        --> Portfolios Formed on Net Share Issues \
        --> Portfolios Formed on Market Beta \
        --> Portfolios Formed on Residual Variance \
        After download, use "Lo 10" - "Hi 10"

2. Liquidity (automatically by "data_from_website.py")
- website: https://finance.wharton.upenn.edu/~stambaug/liq_data_1962_2023.txt

    --- Column 4: Traded liquidity factor (LIQ_V, 10-1 portfolio return) use as LIQ Factor \

    --- (Tips: Column 2: Levels of aggregated liquidity (Figure 1 in the paper) use as Macro predictor named as "x_ill"

3. AQR Factors
- (1) HMLM
    --- website: https://www.aqr.com/Insights/Datasets/The-Devil-in-HMLs-Details-Factors-Monthly

- (2) QMJ
    --- website: https://www.aqr.com/Insights/Datasets/Quality-Minus-Junk-Factors-Monthly

- (3) BAB
    --- website: https://www.aqr.com/Insights/Datasets/Betting-Against-Beta-Equity-Factors-Monthly

4. IA, ROE, REG
- website: https://global-q.org/factors.html

    --> The q-factors and Expected Growth Factor

5. PEAD, FIN
- website: https://docs.google.com/spreadsheets/d/1kHa6UWQYPwmg0zORh0KgnlO6fBDakfIO/edit#gid=1767442868

6. SUE
- website: https://global-q.org/testingportfolios.html

- Download HXZ's 1-way sorts "ivff" (anomaly in Frictions) and "sue" (anomaly in Momentum) \
    --- then use quantile 10 - quantile 1 to obtain the anomaly results

7. Intermediary (IMD)
- website: https://zhiguohe.net/data-and-empirical-patterns/intermediary-capital-ratio-and-risk-factor/

- Use the 3rd column --> "intermediary_value_weighted_investment_return"
