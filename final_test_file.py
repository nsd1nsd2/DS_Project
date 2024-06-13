import matplotlib.pyplot as plt 
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
    plt.title("Yearly Average of CO2 Emission")
    plt.yscale('log')
    plt.xticks(rotation = 90)
    plt.savefig('year.png', bbox_inches = 'tight')
    plt.show()
    return year_emission

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

def visual_seasonal(year,season,country):
    seasonal_emission = {

    }
    seasonal_winter = ['December', 'January','February']
    seasonal_spring = ['March', 'April','May']
    seasonal_summer = ['June', 'July', 'August']
    seasonal_fall = ['September', 'October','November']
    seasonal_emission = read_file_yearly(year)
    if season == "winter":
        plt.bar(seasonal_winter, (seasonal_emission[country][0:3]), width= 0.2)
        plot_style(country)
    if season == "spring":
        plt.bar(seasonal_spring, (seasonal_emission[country][3:6]), width= 0.5)
        plot_style(country)
    if season == "summer":
        plt.bar(seasonal_summer, (seasonal_emission[country][6:9]), width= 0.5)
        plot_style(country)
    if season == 'fall':
        plt.bar(seasonal_fall, (seasonal_emission[country][9:12]), width= 0.5)
        plot_style(country)
    

print(read_file_yearly('2020.csv'))         
visual_seasonal('2020.csv', 'winter', 'Switzerland')
#print(visual_yearly('2020.csv'))
#print(visual_monthly('2021.csv','Albania'))
