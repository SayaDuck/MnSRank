import csv

tournies = []
players = []
placements = ['1st', '2nd', '3rd', '4th', '5th', '7th', '9th']

with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        fifthlist = [row[10], row[11]]
        seventhlist = [row[12], row[13]]
        ninthlist = [row[14], row[15]]
        tournies.append({'id': row[0], 'date': row[1], 'name': row[2], 'link': row[3], 'entrants': row[4], 'tier': row[5], '1st': [row[6]], '2nd': [row[7]], '3rd': [row[8]], '4th': [row[9]], '5th': fifthlist, '7th': seventhlist, '9th': ninthlist})
tournies.pop(0)
print(tournies)

with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        for name in row[6:]:
            if name not in [x['name'] for x in players]:
                players.append({'name': name})
                
print(players)