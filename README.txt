1. ani_SWE_NOR_EUR_cases.gif
Animation showing the trend of COVID-19 cases per one million people in Sweden, Europe, and the Nordic countries.
-data: europe_avg.csv the table that contains statistics about new cases and deaths in european countries per 1mln.
-source: made from WHO-COVID-19-global-data.csv (official WHO website) and API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv (official World Bank website)
-modification I used: Normalisation of data per one milion of people weekly_per_100['New_cases'] / weekly_per_100['population'] * 1000000

2. ani_SWE_NOR_EUR_deaths.gif
Animation showing the trend of COVID-19 deaths per one million people in Sweden, Europe, and the Nordic countries.
-data: europe_avg.csv the table that contains statistics about new cases and deaths in european countries.
-source: made from WHO-COVID-19-global-data.csv (official WHO website) and API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv (official World Bank website)
-modification I used: Normalisation of data per one milion of people weekly_per_100['New_deaths'] / weekly_per_100['population'] * 1000000

3. multiple_plots_cases.png
Subplots showing the trends of COVID-19 cases in the Nordic region.
data: cases_per_100.csv the table that contains information about new cases and deaths in european countries per 1mln.
-source: made from WHO-COVID-19-global-data.csv (official WHO website) and API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv (official World Bank website)
-modification I used: Normalisation of data per one milion of people weekly_per_100['New_cases'] / weekly_per_100['population'] * 1000000

4. multiple_plots_deaths.png
Subplots showing the trends of COVID-19 deaths in the Nordic region.
data: cases_per_100.csv the table that contains information about new cases and deaths in european countries per 1mln.
-source: made from WHO-COVID-19-global-data.csv (official WHO website) and API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv (official World Bank website)
-modification I used: Normalisation of data per one milion of people weekly_per_100['New_deaths'] / weekly_per_100['population'] * 1000000

5. plotly-BAR-deaths_age.html
Interactive bar plot showing the number of deaths per 100K in age groups over 70.
data: SWEDEN-AGE-GROUPS-DEATHS_per100K.csv-the table which contains information about number of deaths in age groups above 70 in Sweden
source: data made from DEATH03_20250519-105035.xlsx which is from https://pxweb.nhwstat.org/Prod/pxweb/en/NHWSTAT/

6. plotly-stack-bar-comparison.html
Interactive stacked bar plot showing the number of deaths due to COVID-19 and other causes per 100K in Sweden and the European average.
data: comparison-SWE-DEN-NOR.csv-the table which contains information about sweden and average of Denmark and Norway of Covid and Non Covid deaths
source: Sweden_deaths_covid_normal.xlsx, Norway_deaths_covid_normal.xlsx, Denmark_deaths_covid_normal.xlsx which are from https://pxweb.nhwstat.org/Prod/pxweb/en/NHWSTAT/

7. plot_inflation_SWE_NOR.png
Plot showing the infaltion in Sweden and average of Nordic countries along 2010-2024
data: API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_37769.csv-the table that contains information about inflacy in countries among the World
source: World Bank

8. plot_inflation_SWE_EUR.png
Plot showing the infaltion in Sweden and average of European countries along 2010-2024
data: API_FP.CPI.TOTL.ZG_DS2_en_csv_v2_37769.csv-the table that contains information about inflacy in countries among the World
source: World Bank
modification: count average of european countries

9. plot_unemployment_SWE_EUR.png
Plot showing the unemployment rate in Sweden and average of European countries along 2010-2024
data: Unemployment_Rate.csv-the table that contains information about unemployment rate in countries among the World
source: API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_38061.csv World Bank
modification: count average of european countries

10. plot_unemployment_SWE_NOR.png
data: Unemployment_Rate.csv-the table that contains information about unemployment rate in countries among the World
source: API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_38061.csv World Bank

11. plot_vaccine_doses_SWE.png
data: cumulative-covid-vaccinations.csv the table that contains information about vaccine doses cummulative in Sweden
source: https://ourworldindata.org/covid-vaccinations

12. plot_cummulative_deaths_SWE.png
data: SWEDEN-weekly-cases-deaths.csv-table which contains information about  weekly cases and deaths
source: WHO website

other:
WHO-COVID-19-global-data.csv 
-dataset from WHO website which contains information about basic statistics of Covid-19 pandemic.
-Columns: Date_reported-date of the report 
          Country_code-code of country 
          Country-name of the country 
          WHO_region
          New_cases-number of new cases since the last report 
          Cumulative_cases-number of cumulative cases since the begining of pandemic
          New_deaths-number of deaths since last report
          Cumulative_deaths-number of deaths since the beginig of the pandemic
