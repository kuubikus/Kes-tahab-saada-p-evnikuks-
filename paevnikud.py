import csv
import datetime

# Ava skooride fail
try:
    path = "paevnikud.csv"
    with open(path,newline='',encoding="UTF-8-sig") as f:
        date = f.readline()
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]
except FileNotFoundError:
    # Tee uus fail
    print("Sisesta uue faili asukoht")
    path = input()
    # Loo uus nimestu
    with open(path,newline='',encoding="UTF-8-sig") as f:
        date = f.readline()
        csv_reader = csv.DictReader(f)
        data = [row for row in csv_reader]

# Vii muudatused sisse. Kui oli päevnik, siis +10. Motivatsioon vastavalt rikkumisele
date = datetime.date.today()
for paevnik in data:
    paevnik['Skoor'] = int(paevnik['Skoor'])
    paevnik['Motivatsioon'] = int(paevnik['Motivatsioon'])
    if paevnik['Oli päevnik?'] == "x":
        if date.weekday() < 5:
            paevnik['Skoor'] += 10  # Tööpäev
        else:
            paevnik['Skoor'] += 15  # Nädalavahetus
        paevnik['Oli päevnik?'] = None
    paevnik['Skoor'] -= paevnik['Motivatsioon']
    paevnik['Motivatsioon'] = 0 # Reset järgmiseks päevaks

# Järjekord skoori järgi
sorted_data = sorted(data, key=lambda d: d['Skoor'])

# Uuenda tabel
header = data[0].keys()
date_dict = {'Nimi':date}
with open(path, 'w', newline='',encoding="UTF-8-sig") as f_out:
    writer = csv.DictWriter(f_out, fieldnames=header,restval=None)
    writer.writerow(date_dict)
    writer.writeheader()
    for row in sorted_data:
        writer.writerow(row)
