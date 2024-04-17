import requests
from bs4 import BeautifulSoup
import csv

# Fetch the web page
url = "https://en.wikipedia.org/wiki/List_of_active_Indian_military_aircraft"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table')
tbody = table.find('tbody')
aircraft_data = []
rows = tbody.find_all('tr')
for row in rows[2:]:  # Skipping the first two header rows
    columns = row.find_all('td')
    if len(columns) == 6:
        aircraft_name = columns[0].text.strip()
        origin = columns[1].text.strip()
        aircraft_type = columns[2].text.strip()
        variant = columns[3].text.strip()
        in_service = columns[4].text.strip()
        notes = columns[5].text.strip()
        # Append data to the list
        aircraft_data.append([aircraft_name, origin, aircraft_type, variant, in_service, notes])

csv_file = "indian_military_aircraft.csv"
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Aircraft Name','Origin' ,'Aircraft Type','Variant','In Service', 'Notes'])  # Write header row
    writer.writerows(aircraft_data)

print(f"Data has been written to {csv_file}")