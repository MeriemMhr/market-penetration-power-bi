import json
import csv

# Read JSON from file
with open('parking_ottawa.json') as f:
    data = json.load(f)

# Extract parking lots
parking_lots = data['parking_lots']

# Define CSV file name
csv_file = 'parking_lots.csv'

# Write CSV
with open(csv_file, 'w', newline='') as csvfile:
    fieldnames = parking_lots[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for lot in parking_lots:
        writer.writerow(lot)

# Select columns
columns = ['id','address', 'capacity', 'latitude', 'longitude']

# Include only selected columns
with open(csv_file, 'r') as infile, open('parking_lots_clean.csv', 'w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=columns)
    writer.writeheader()
    for row in reader:
        writer.writerow({col: row[col] for col in columns})


print("CSV file '{}' has been created successfully.".format(csv_file))
