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
    plt.savefig('year.png', bbox_inches = 'tight')
    plt.show()

def visual_monthly(year, country):
    month_emission = {

    }
    months = []
    for i in range(1,13):
        months.append(calendar.month_name[i])
    month_emission = read_file_yearly(year)
    plt.bar(months, month_emission[country])
    plt.title(country.lower().capitalize()+"'s Average CO2 Usage Per Month'")
    plt.ylabel("Amount in tons")
    plt.xticks(fontsize = 8)
    plt.xlabel("Months")
    plt.show()
def plot_style(country):
    plt.xlabel("Months")
    plt.title(country + "'s Seasonal CO2 Emissions")
    plt.ylabel("Average Amount Burned in Tonnes", size = 10)
    plt.show()

def visual_heatmap(df, country):
    # Filtering data for the specified country
    country_df = df[df["STATE_NAME"] == country.upper()]
    
    # Creating heatmap with years as rows and months as columns
    years = country_df["YEAR"].unique()
    months = list(range(1, 13))  # Months from 1 to 12
    heatmap_data = np.zeros((len(years), len(months)))

    # Filtering data for the specific year and month
    for i, year in enumerate(years):
        for j, month in enumerate(months):
            emission = country_df[(country_df["Year"] == year) & (country_df["Month"] == month)]["CO2_QTY_TONNES"]
            if not emission.empty:
                heatmap_data[i, j] = emission.values[0]
    
    # Plotting the heatmap
    plt.figure(figsize=(12, 8))
    plt.imshow(heatmap_data, cmap="YlGnBu")
    plt.colorbar(label="CO2 Emissions (Tons)")
    plt.title(f"Seasonal CO2 Emissions Heatmap for {country.title()} (2020-2023)")
    plt.xlabel("Month")
    plt.ylabel("Year")
    plt.xticks(ticks=np.arange(len(months)), labels=calendar.month_abbr[1:], rotation=45)
    plt.yticks(ticks=np.arange(len(years)), labels=years)
    plt.show()


    
def main():
    # Plotting yearly for 2020 to 2023
    for years in range(2020, 2024):
        visual_yearly(str(years) + ".csv")
    
    # Loading CSV files into dataframes and combining
    files = ["2020.csv", "2021.csv", "2022.csv", "2023.csv"]
    dataframes = [pd.read_csv(file) for file in files]
    combined_df = pd.concat(dataframes)
    
    # Filtering data for Albania and Bosnia and Herzegovina
    countries_df = combined_df[combined_df["STATE_NAME"].isin(["ALBANIA", "BOSNIA AND HERZEGOVINA"])]

    # Getting monthly emissions
    monthly_emissions_countries = countries_df.groupby(["YEAR", "MONTH", "STATE_NAME"])["CO2_QTY_TONNES"].mean().reset_index()
    
    # Define a color map for the years to differentiate them in the plot
    colors = {2020: 'b', 2021: 'g', 2022: 'r', 2023: 'm'}

    # Albania Plot
    plt.figure(figsize=(16, 10))
    for year in monthly_emissions_countries['YEAR'].unique():
        albania_data = monthly_emissions_countries[(monthly_emissions_countries['STATE_NAME'] == 'ALBANIA') & (monthly_emissions_countries['YEAR'] == year)]
        plt.plot(albania_data['MONTH'], albania_data['CO2_QTY_TONNES'], color=colors[year], label=f'Albania {year}')
    plt.title('Monthly CO2 Emissions for Albania (2020-2023)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('CO2 Emissions (Tonnes)', fontsize=14)
    plt.legend(title='Year')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Bosnia Plot
    plt.figure(figsize=(16, 10))
    for year in monthly_emissions_countries['YEAR'].unique():
        bosnia_data = monthly_emissions_countries[(monthly_emissions_countries['STATE_NAME'] == 'BOSNIA AND HERZEGOVINA') & (monthly_emissions_countries['YEAR'] == year)]
        plt.plot(bosnia_data['MONTH'], bosnia_data['CO2_QTY_TONNES'], color=colors[year], label=f'Bosnia and Herzegovina {year}')
    plt.title('Monthly CO2 Emissions for Bosnia and Herzegovina (2020-2023)', fontsize=16)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('CO2 Emissions (Tonnes)', fontsize=14)
    plt.legend(title='Year')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    
    # Generating heatmaps for Albania and Bosnia
    visual_heatmap(combined_df, 'Albania')
    visual_heatmap(combined_df, 'Bosnia And Herzegovina')
if __name__ == "__main__":
    main()