import csv

tournies = []

with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        fifthlist = [row[9], row[10]]
        seventhlist = [row[11], row[12]]
        ninthlist = [row[13], row[14]]
        tournies.append({'date': row[0], 'name': row[1], 'link': row[2], 'entrants': row[3], 'tier': row[4], '1st': row[5], '2nd': row[6], '3rd': row[7], '4th': row[8], '5th': fifthlist, '7th': seventhlist, '9th': ninthlist})
tournies.pop(0)
print(tournies)

