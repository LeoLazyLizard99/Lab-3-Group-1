import csv
''''''
with open('country_full.csv', 'r', newline='', encoding='utf-8') as f:
    rows = csv.DictReader(f)

    for row in rows:
        region = row['region'] or 'Antarctica'

        with open(f'regions/{region}.csv', 'a', newline='', encoding='utf-8') as output:
            writer = csv.writer(output)
            writer.writerow([row['name'], region])