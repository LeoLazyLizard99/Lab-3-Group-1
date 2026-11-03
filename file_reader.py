import csv

with open('country_full.csv', 'r') as f:
    regions = []
    out = []
    data = []

    rows = csv.DictReader(f)

    for row in rows:
        regions.append(row['region'])
        a = out.append(row['name'])
        b = out.append(row['region'])
        data.append[1,2]

    for region in set(regions):
        if region == "":
            region = "Antarctica"

        print(f"creating a file for: {region}...")

        with open(f"regions/{region}.csv", 'w') as region:
            print(f"writing {out} to {region.name}...")
            writer = csv.writer(region)
            writer.writerows(out)
    

