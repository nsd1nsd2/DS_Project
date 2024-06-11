import matplotlib.pyplot as plt 
import statistics as sta

def read_file_yearly(filename):
    year_emission = {
        
    }
    
    file = open(filename, 'r')
    line = file.readline().strip()
    for line in file: 
        val = line.split(',')
        country = val[2]
        emission = val[4]
        if country not in year_emission:
            year_emission[country] = []
        if emission not in country:
            year_emission[country].append(float(emission))
    for key in list(year_emission.keys()):
        if len(year_emission[key]) != 12:
            del year_emission[key]
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

def visual_monthly(year):
    month_emission = {

    }
    month_emission = read_file_yearly(year)
    

print(visual_yearly('2020.csv'))
print(visual_yearly('2021.csv'))
print(visual_yearly('2022.csv'))
print(visual_yearly('2023.csv'))