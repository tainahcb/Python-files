""" 
Author: Tainah Correia Barreto
Project W06 Data Analysis
"""

print("Hello!")
print("This program allows the user to analyze the dataset by finding the year and country with the lowest life expectancy,\nthe year and country with the highest life expectancy, and the average life expectancy for a given year.")
print("It also finds the country with the minimum and the one with the maximum life expectancies for that year.")
print("Additionally, it allows the user to input a country and view the minimum, maximum, and average life expectancy for that country.")
print("Finally, it searches for anomalies or interesting patterns in the data.")
print()

import csv
import statistics

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

country_of_interest = input("Enter the country of interest: ")

country_data = [item for item in data if item['Entity'] == country_of_interest]

min_life_expectancy = float('inf')
max_life_expectancy = float('-inf')

for item in country_data:
    if float(item['Life expectancy (years)']) < min_life_expectancy:
        min_life_expectancy = float(item['Life expectancy (years)']) 
