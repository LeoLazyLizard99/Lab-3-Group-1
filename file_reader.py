import csv

groups = {}

with open('country_full.csv', 'r') as f:
    rows = csv.DictReader(f)

    for row in rows:
        region = row['region']
        if region == "":
            region = "Antarctica"

        if region not in groups:
            groups[region] = []

        groups[region].append([row['name'], region])

for region, region_rows in groups.items():
    print(f"creating a file for: {region}...")

    with open(f"regions/{region}.csv", 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(['name','region'])
        writer.writerows(region_rows)

    print(f"wrote {len(region_rows)} rows to regions/{region}.csv")