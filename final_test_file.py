import matplotlib.pyplot as plt 
import statistics as sta
import calendar
import seaborn as sns 
colors = ['red', 'green', 'yellow','blue','turquoise','magenta','black','purple', 'pink','gold','crimson','tan']

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
    sns.barplot(x = country, y = average, palette='magma')
    for i in range(len(country)):
        plt.text(i,average[i],round(average[i]), ha='center', va='bottom',fontsize=5)
    plt.ylabel("Average emission in pounds")
    plt.xlabel("Countries")
    if year == "2020.csv":
        plt.title("Yearly Average of CO2 Emission in 2020" )
    if year == "2021.csv":
        plt.title("Yearly Average of CO2 Emission in 2021" )
    if year == "2022.csv":
        plt.title("Yearly Average of CO2 Emission in 2022" )
    if year == "2023.csv":
        plt.title("Yearly Average of CO2 Emission in 2023" )
    plt.yscale('log')
    plt.xticks(rotation = 90)
    plt.savefig(year + '.png', bbox_inches = 'tight')
    plt.show()
    return year_emission

def visual_monthly(year, country):
    month_emission = {

    }
    months = []
    for i in range(1,13):
        months.append(calendar.month_name[i])
    month_emission = read_file_yearly(year)
    plt.figure(figsize=(18,6),dpi=200)
    sns.barplot(x=months,y=month_emission[country], palette= 'rocket')
    for i in range(len(month_emission[country])):
        plt.text(i,month_emission[country][i], round(month_emission[country][i]), ha='center', va='bottom',fontsize = 8)
    if year == "2020.csv":
        plt.title(country.lower().capitalize()+"'s 2020 Average CO2 Usage Per Month")
    if year == "2021.csv":
        plt.title(country.lower().capitalize()+"'s 2021 Average CO2 Usage Per Month")
    if year == '2022.csv':
        plt.title(country.lower().capitalize()+"'s 2022 Average CO2 Usage Per Month")
    plt.ylabel("Amount in tons")
    plt.xticks(fontsize = 8)
    plt.xlabel("Months")
    plt.savefig(country + year +'.png')
    plt.show()

def plot_style(country,year):
    plt.xlabel("Months")
    if year == "2020.csv":
        plt.title(country + "'s 2020 Seasonal CO2 Emissions")
    if year == "2021.csv":
        plt.title(country + "'s 2021 Seasonal CO2 Emissions")
    if year == "2022.csv":
        plt.title(country + "'s 2022 Seasonal CO2 Emissions")
    if year == "2023.csv":
        plt.title(country + "'s 2023 Seasonal CO2 Emissions")
    plt.ylabel("Average Amount Burned in Tonnes", size = 10)
    plt.show()

def visual_seasonal(year,season,country):
    seasonal_emission = {

    }
    seasonal_winter = ['December', 'January','February']
    seasonal_spring = ['March', 'April','May']
    seasonal_summer = ['June', 'July', 'August']
    seasonal_fall = ['September', 'October','November']
    seasonal_emission = read_file_yearly(year)
    if season == "winter":
        sns.barplot(x=seasonal_winter, y=seasonal_emission[country][0:3], palette="mako")
        plot_style(country)
    if season == "spring":
        sns.barplot(x=seasonal_spring, y=seasonal_emission[country][3:6], palette='crest')
        plot_style(country)
    if season == "summer":
        sns.barplot(x=seasonal_summer, y=seasonal_emission[country][6:9], palette='magma')
        plot_style(country)
    if season == 'fall':
        sns.barplot(x=seasonal_fall, y=seasonal_emission[country][9:12],palette='flare')
        plot_style(country)
#visual_yearly("2020.csv")
#visual_yearly('2021.csv')
#visual_yearly('2022.csv')
visual_monthly('2020.csv', "Albania")
visual_monthly('2021.csv', "Albania")
visual_monthly('2022.csv', "Albania")
visual_monthly('2020.csv', "Germany")
visual_monthly('2021.csv', "Germany")
visual_monthly('2022.csv', "Germany")
#visual_monthly('2020.csv','France')
#visual_seasonal('2020.csv','winter',"Albania")
