import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
import statistics as sta
import calendar
    
emission = {
    }

def read_file_yearly(filename):
    year_emission = {
        
    }
    
    file = open(filename, 'r')
    line = file.readline().strip()
    for line in file: 
        val = line.split(',')
        country = val[2].lower().capitalize()
        emission = val[4]
        if country not in year_emission:
            year_emission[country] = []
        if emission not in country:
            year_emission[country].append(float(emission))
    for key in list(year_emission.keys()):
        if len(year_emission[key]) != 12:
            del year_emission[key]
    emission = year_emission
    return year_emission

def visual_yearly(year):
    year_emission = {
}
    country = []
    average = []
    year_emission = read_file_yearly(year)
    
    for key, value in year_emission.items():
        country.append(key)
        average.append(sta.mean(value))
    plt.figure(figsize=(18,6), dpi=200)
    plt.bar(country, average)
    plt.ylabel("Average emission in pounds")
    plt.xlabel("Countries")
    plt.title(f"Yearly Average of CO2 Emission ({year.replace('.csv', '')})")
    plt.yscale('log')
    plt.xticks(rotation = 90)
    plt.show()

def visual_monthly(combined_df, country):
    # Getting years from dataframe
    years = combined_df["YEAR"].unique()
    
    # Colors for plotting
    colors = {2020: 'b', 2021: 'g', 2022: 'r', 2023: 'm'}

    # Plotting for specified country
    plt.figure(figsize=(16, 10))
    for year in years:
        country_data = combined_df[(combined_df['STATE_NAME'] == country.upper()) & (combined_df['YEAR'] == year)]
        plt.plot(country_data['MONTH'], country_data['CO2_QTY_TONNES'], color=colors[year], label=f'{country.title()} {year}')
    plt.title(f'Monthly CO2 Emissions for {country.title()} (2020-2023)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('CO2 Emissions (Tonnes)', fontsize=14)
    plt.legend(title='Year')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
def visual_heatmap(df, country):
    # Filtering data for the specified country
    country_df = df[df["STATE_NAME"] == country.upper()]
    
    # Creating heatmap with years as rows and months as columns
    years = country_df["YEAR"].unique()
    months = list(range(1, 13))  # Months from 1 to 12
    heatmap_data = np.zeros((len(years), len(months)))

    
    for i, year in enumerate(years):
        for j, month in enumerate(months):
            emission = country_df[(country_df["Year"] == year) & (country_df["Month"] == month)]["CO2_QTY_TONNES"]
            if not emission.empty:
                heatmap_data[i, j] = emission.values[0]
    
    # Plotting the heatmap
    plt.figure(figsize=(12, 8))
    plt.imshow(heatmap_data, cmap="YlGnBu")
    plt.colorbar(label="CO2 Emissions (Tons)")
    plt.title(f"CO2 Emissions Heatmap for {country} (2020-2023)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.xticks(ticks=np.arange(len(months)), labels=calendar.month_abbr[1:], rotation=45)
    plt.yticks(ticks=np.arange(len(years)), labels=years)
    plt.show()

def main():
    
    # Plotting yearly for 2020 to 2023
    for years in range(2020, 2024):
        visual_yearly(f"{years}.csv")
    
    # Creating combined dataframes of csv files for plotting
    files = ["2020.csv", "2021.csv", "2022.csv", "2023.csv"]
    dataframes = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(dataframes)
    
    # Plotting monthly for Albania and Bosnia (2020 - 2023)
    countries = ["Albania", "Bosnia And Herzegovina"]
    for country in countries:
        visual_monthly(combined_df, country)
        
    # Plotting heatmaps for Albania and Bosnia (2020 -2023)
    visual_heatmap(combined_df, 'Albania')
    visual_heatmap(combined_df, 'Bosnia And Herzegovina')

if __name__ == "__main__":
    main()