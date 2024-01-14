"""
Author: Tainah Correia Barreto
Project W06 Data Analysis
"""
# I added three extra features to show creativity:
# - A function to find the year and country that has the largest drop from one year to the next in life expectancy
# - A function to allow the user to enter a country and then show the minimum, maximum and average life expectancy for that country
# - A search for anomalies or interesting patterns in the data

print("Hello!")
print("This program allows the user to analyze the dataset by finding the year and country with the lowest life expectancy,\nthe year and country with the highest life expectancy, and the average life expectancy for a given year.")
print("It also finds the country with the minimum and the one with the maximum life expectancies for that year.")
print("Additionally, it finds the year and country that has the largest drop in life expectancy from one year to the next,\nthe minimum, maximum and average life expectancy for a given country, and some interesting patterns or anomalies in the data.")
print()

import csv

def read_csv_file(file_name):
    data = []
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            data.append(dict(zip(headers, row)))
    return data

data = read_csv_file('life-expectancy.csv')


lowest_life_expectancy = float('inf')
highest_life_expectancy = float('-inf')
lowest_life_expectancy_country = ''
highest_life_expectancy_country = ''
lowest_life_expectancy_year = ''

for item in data:
    if float(item['Life expectancy (years)']) < lowest_life_expectancy:
        lowest_life_expectancy = float(item['Life expectancy (years)'])
        lowest_life_expectancy_country = item['Entity']
        lowest_life_expectancy_year = item['Year']
    if float(item['Life expectancy (years)']) > highest_life_expectancy:
        highest_life_expectancy = float(item['Life expectancy (years)'])
        highest_life_expectancy_country = item['Entity']
        highest_life_expectancy_year = item['Year']

print(f"The overall max life expectancy is: {highest_life_expectancy} from {highest_life_expectancy_country} in {highest_life_expectancy_year}")
print(f"The overall min life expectancy is: {lowest_life_expectancy} from {lowest_life_expectancy_country} in {lowest_life_expectancy_year}")

year_of_interest = input("Enter the year of interest: ")

average_life_expectancy = 0
min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')
min_life_expectancy_country = ''
max_life_expectancy_country = ''

for item in data:
    if item['Year'] == year_of_interest:
        average_life_expectancy += float(item['Life expectancy (years)'])
        if float(item['Life expectancy (years)']) < min_life_expectancy:
            min_life_expectancy = float(item['Life expectancy (years)'])
            min_life_expectancy_country = item['Entity']
        if float(item['Life expectancy (years)']) > max_life_expectancy:
            max_life_expectancy = float(item['Life expectancy (years)'])
            max_life_expectancy_country = item['Entity']

average_life_expectancy /= len(data)

print(f"\nFor the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {average_life_expectancy:.3f}")
print(f"The max life expectancy was in {max_life_expectancy_country} with {max_life_expectancy}")
print(f"The min life expectancy was in {min_life_expectancy_country} with {min_life_expectancy}")

# I added this function to find the year and country that has the largest drop in life expectancy from one year to the next
def find_largest_drop(data):
    largest_drop = 0
    largest_drop_country = ''
    largest_drop_year = ''
    for i in range(len(data) - 1):
        if data[i]['Entity'] == data[i + 1]['Entity']:
            drop = float(data[i]['Life expectancy (years)']) - float(data[i + 1]['Life expectancy (years)'])
            if drop > largest_drop:
                largest_drop = drop
                largest_drop_country = data[i]['Entity']
                largest_drop_year = data[i]['Year']
    return largest_drop, largest_drop_country, largest_drop_year

largest_drop, largest_drop_country, largest_drop_year = find_largest_drop(data)

print(f"\nThe year and country that has the largest drop in life expectancy from one year to the next is:")
print(f"{largest_drop_country} in {largest_drop_year} with a drop of {largest_drop:.3f}")

# I added this function to allow the user to enter a country and then show the minimum, maximum and average life expectancy for that country
def find_country_stats(data, country):
    min_life_expectancy = float('inf')
    max_life_expectancy = float('-inf')
    average_life_expectancy = 0
    min_life_expectancy_year = ''
    max_life_expectancy_year = ''
    count = 0
    for item in data:
        if item['Entity'] == country:
            count += 1
            average_life_expectancy += float(item['Life expectancy (years)'])
            if float(item['Life expectancy (years)']) < min_life_expectancy:
                min_life_expectancy = float(item['Life expectancy (years)'])
                min_life_expectancy_year = item['Year']
            if float(item['Life expectancy (years)']) > max_life_expectancy:
                max_life_expectancy = float(item['Life expectancy (years)'])
                max_life_expectancy_year = item['Year']
    if count > 0:
        average_life_expectancy /= count
        return min_life_expectancy, max_life_expectancy, average_life_expectancy, min_life_expectancy_year, max_life_expectancy_year
    else:
        return None

country_of_interest = input("\nEnter the country of interest: ")

country_stats = find_country_stats(data, country_of_interest)

if country_stats is not None:
    print(f"\nFor the country {country_of_interest}:")
    print(f"The minimum life expectancy was {country_stats[0]:.3f} in {country_stats[3]}")
    print(f"The maximum life expectancy was {country_stats[1]:.3f} in {country_stats[4]}")
    print(f"The average life expectancy was {country_stats[2]:.3f}")
else:
    print(f"\nSorry, I could not find any data for the country {country_of_interest}")

# I searched for anomalies or interesting patterns in the data and found some. Here are some examples:

# I found that the life expectancy in Russia dropped drastically between 1991 and 1994, probably due to the dissolution of the Soviet Union
russia_1991 = 0
russia_1994 = 0
for item in data:
    if item['Entity'] == 'Russia':
        if item['Year'] == '1991':
            russia_1991 = float(item['Life expectancy (years)'])
        if item['Year'] == '1994':
            russia_1994 = float(item['Life expectancy (years)'])

russia_drop = russia_1991 - russia_1994

print(f"\nAn interesting pattern I found is that the life expectancy in Russia dropped drastically between 1991 and 1994 by {russia_drop:.3f} years, probably due to the dissolution of the Soviet Union")

# I found that the life expectancy in Ethiopia increased significantly between 2000 and 2015, probably due to improved health conditions and development
ethiopia_2000 = 0
ethiopia_2015 = 0
for item in data:
    if item['Entity'] == 'Ethiopia':
        if item['Year'] == '2000':
            ethiopia_2000 = float(item['Life expectancy (years)'])
        if item['Year'] == '2015':
            ethiopia_2015 = float(item['Life expectancy (years)'])

ethiopia_increase = ethiopia_2015 - ethiopia_2000

print(f"\nAnother interesting pattern I found is that the life expectancy in Ethiopia increased significantly between 2000 and 2015 by {ethiopia_increase:.3f} years, probably due to improved health conditions and development")
