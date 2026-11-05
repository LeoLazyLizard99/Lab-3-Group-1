import csv
import exceptions as exc

# CIS-117 Lab3
# Takes the country_full.csv file and sorts the countries into regions and only keeping the names and regions in each file
# Group 1
# Florian Rabe, Colton Feige
# we both worked on the main file and then I (Florian) made a seperate exceptions file for the try and except function.

exc.read_file("country_full")

with open('country_full.csv', 'r', newline='', encoding='utf-8') as f:
    rows = csv.DictReader(f)

    for row in rows:
        region = row['region'] or 'Antarctica'

        with open(f'regions/{region}.csv', 'a', newline='',  encoding='utf-8') as output:
            writer = csv.writer(output)
            writer.writerow([row['name'], region])