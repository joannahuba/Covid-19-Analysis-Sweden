import pandas as pd
import pycountry as pg
import pycountry_convert as pc

countries = {country.name for country in pg.countries}

# weekly Sweden (new cases, deaths)
weekly_swe = pd.read_csv("../csv/WHO-COVID-19-global-data.csv")
weekly_swe = weekly_swe.fillna(0)
weekly_swe = weekly_swe[weekly_swe["Country"] == "Sweden"]
weekly_swe.to_csv("../csv/SWEDEN-weekly-cases-deaths.csv")

# daily Sweden (new cases, deaths)
daily_swe = pd.read_csv("../csv/WHO-COVID-19-global-daily-data.csv")
daily_swe = daily_swe[daily_swe["Country"] == "Sweden"]
daily_swe = daily_swe.fillna(0)

# new cases and deaths per 100 th people
weekly_world = pd.read_csv("../csv/WHO-COVID-19-global-data.csv")
population = pd.read_csv("../csv/API_SP.POP.TOTL_DS2_en_csv_v2_76253.csv", skiprows=4).drop(['Unnamed: 68'], axis=1)

population = population[population['Country Name'].isin(countries)]
population = population.iloc[:, [0, 1] + list(range(64, population.shape[1]-1))]
population = population.melt(
    id_vars=['Country Name', 'Country Code'],
    value_vars=['2020', '2021', '2022'],
    var_name='year',     
    value_name='population'   
)
population['year'] = population['year'].astype(int)

weekly_world['Date_reported'] = pd.to_datetime(weekly_world['Date_reported'])
weekly_world = weekly_world.dropna()
weekly_world['year'] = weekly_world['Date_reported'].dt.year

# merge two df
weekly_per_100 = weekly_world.merge(population[['Country Name', 'year', 'population']], left_on=['Country', 'year'], right_on=['Country Name', 'year'], how='left')
weekly_per_100 = weekly_per_100.dropna()

weekly_per_100["cases_per_100"] = weekly_per_100['New_cases'] / weekly_per_100['population'] * 1000000
weekly_per_100["deaths_per_100"] = weekly_per_100['New_deaths'] / weekly_per_100['population'] * 1000000
del weekly_per_100["Country Name"]
del weekly_per_100["WHO_region"]
weekly_per_100.to_csv("../csv/cases_per_100.csv")

# average Europe  per 100 th
def is_european_country(country):
    try:
        country_alpha2 = pg.countries.get(name=country).alpha_2
        continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        return continent_code == 'EU'
    except:
        return False

european_countries = [country.name for country in pg.countries if is_european_country(country.name)]
europe_avg = weekly_per_100[weekly_per_100["Country"].isin(european_countries)]
europe_avg = weekly_per_100.groupby(by=["Date_reported"], as_index=False)[["deaths_per_100" ,"cases_per_100", "New_cases", "New_deaths"]].mean()

europe_avg.to_csv("../csv/europe_avg.csv")

# Sweden deaths by age
men_women_age = pd.read_excel(
    '../csv/DEATH03_20250519-105035.xlsx',
    usecols='A:D',
    skiprows=3,
    nrows=33,
    engine='openpyxl'
)

men_women_age.columns = ['year', 'gender', 'age_group', 'deaths_per_100K']
del men_women_age['gender']
men_women_age['year'] = men_women_age['year'].ffill()
men_women_age['year'] = men_women_age['year'].astype(int)

men_women_age.to_csv("../csv/SWEDEN-AGE-GROUPS-DEATHS_per100K.csv")


# table to compare deaths
sweden = pd.read_excel("../csv/Sweden_deaths_covid_and _normal.xlsx",
                       usecols='A:E',
                       skiprows=3,
                       nrows=4,
                       engine='openpyxl')
norway = pd.read_excel("../csv/Norway_deaths_covid_normal.xlsx",
                       usecols='A:E',
                       skiprows=3,
                       nrows=4,
                       engine='openpyxl')
denmark = pd.read_excel("../csv/Denmark_deaths_covid_normal.xlsx",
                        usecols='A:E',
                       skiprows=3,
                       nrows=4,
                       engine='openpyxl')

del sweden['Unnamed: 1']
del sweden['Unnamed: 2']
sweden = sweden.rename(columns={"Unnamed: 0": "year", "COVID-19 (U07.1-U12.9)": "SWE-COVID-19_deaths", "All causes of death (A00-Y89)": "SWE-all_deaths"})

del norway['Unnamed: 1']
del norway['Unnamed: 2']
norway = norway.rename(columns={"Unnamed: 0": "year", "COVID-19 (U07.1-U12.9)": "COVID-19_deaths", "All causes of death (A00-Y89)": "all_deaths"})

del denmark['Unnamed: 1']
del denmark['Unnamed: 2']
denmark = denmark.rename(columns={"Unnamed: 0": "year", "COVID-19 (U07.1-U12.9)": "COVID-19_deaths", "All causes of death (A00-Y89)": "all_deaths"})
nor_den_avg = pd.concat([norway, denmark])
nor_den_avg = nor_den_avg.groupby(by="year", as_index=False)[["COVID-19_deaths", "all_deaths"]].mean()
nor_den_avg = nor_den_avg.rename(columns={"COVID-19_deaths": "COVID-19_deaths_nor_den", "all_deaths": "all_deaths_nor_den"})

comparison = sweden.merge(nor_den_avg[['year', 'COVID-19_deaths_nor_den', 'all_deaths_nor_den']], left_on=['year'], right_on=['year'], how='left')
comparison.to_csv("../csv/comparison-SWE-DEN-NOR.csv")

# Unemployment rate table
unemployment = pd.read_csv("../csv/API_SL.UEM.TOTL.ZS_DS2_en_csv_v2_38061.csv", skiprows=4)
unemployment_eur = unemployment[unemployment['Country Name'].isin(european_countries)]
del unemployment_eur['Indicator Name']
del unemployment_eur['Unnamed: 69']
del unemployment_eur['Indicator Code']
unemployment_eur = unemployment_eur.loc[:, ["Country Name", "Country Code"] + list(unemployment_eur.loc[:, "2010":].columns)]
unemployment_eur = unemployment_eur.dropna()
unemployment_eur.to_csv("../csv/Unemployment_Rate.csv")
