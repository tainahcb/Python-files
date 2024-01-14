import csv
def read_csv_file(filename):
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
def find_lowest_life_expectancy(data):
    lowest_life_expectancy = float('inf')
    lowest_life_expectancy_country = ''
    for item in data:
        if float(item['Life expectancy']) < lowest_life_expectancy:
            lowest_life_expectancy = float(item['Life expectancy'])
            lowest_life_expectancy_country = item['Country']
    return lowest_life_expectancy, lowest_life_expectancy_country
def find_average_life_expectancy(data, year):
    average_life_expectancy = 0
    for item in data:
        if item['Year'] == year:
            average_life_expectancy += float(item['Life expectancy'])
    average_life_expectancy /= len(data)
    return average_life_expectancy
def find_max_and_min_life_expectancy(data, year):
    max_life_expectancy = float('-inf')
    min_life_expectancy = float('inf')
    max_life_expectancy_country = ''
    min_life_expectancy_country = ''
    for item in data:
        if item['Year'] == year:
            if float(item['Life expectancy']) > max_life_expectancy:
                max_life_expectancy = float(item['Life expectancy'])
                max_life_expectancy_country = item['Country']
            if float(item['Life expectancy']) < min_life_expectancy:
                min_life_expectancy = float(item['Life expectancy'])
                min_life_expectancy_country = item['Country']
    return max_life_expectancy, max_life_expectancy_country, min_life_expectancy, min_life_expectancy_country
def main():
    data = read_csv_file('life-expectancy.csv')
    lowest_life_expectancy, lowest_life_expectancy_country = find_lowest_life_expectancy(data)