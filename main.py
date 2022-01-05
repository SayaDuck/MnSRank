import csv

tournies = []
players = []
placements = ['1st', '2nd', '3rd', '4th', '5th', '7th', '9th']
points = { 1: {'1st': 15, '2nd': 13, '3rd': 10, '4th': 8, '5th': 7, '7th': 6, '9th': 5}, 2: {'1st': 10, '2nd': 8, '3rd': 7, '4th': 6, '5th': 5, '7th': 3, '9th': 2}, 3: {'1st': 5, '2nd': 3, '3rd': 2, '4th': 1, '5th': 0, '7th': 0, '9th': 0}, 4: {'1st': 4, '2nd': 2, '3rd': 1, '4th': 0, '5th': 0, '7th': 0, '9th': 0}, 5: {'1st': 1, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0, '7th': 0, '9th': 0} }

# populate tournaments dict
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        fifthlist = [row[10], row[11]]
        seventhlist = [row[12], row[13]]
        ninthlist = [row[14], row[15]]
        tournies.append({'id': row[0], 'date': row[1], 'name': row[2], 'link': row[3], 'entrants': row[4], 'tier': row[5], '1st': [row[6]], '2nd': [row[7]], '3rd': [row[8]], '4th': [row[9]], '5th': fifthlist, '7th': seventhlist, '9th': ninthlist})
        # todo: maybe set up a conditional to remove 0 point placers here based on tourney tier
tournies.pop(0)
print(tournies)

# populate players dict 
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        for name in row[6:]:
            if name not in [x['name'] for x in players]:
                players.append({'name': name, 'placements': []})

print(players)

# placements format:
# {
#   id:
#   place:
#   points:
# }

# maybe list (topplacements) that gets updated every time an new placement is looped through?

for tourney in tournies:
    for place in placements:
        for player in players:
            if player['name'] in tourney[place]:
                tourneyid = tourney['id']
                pointscalc = points[int(tourney['tier'])][place]
                player['placements'].append({'id': tourneyid, 'place': place, 'points': pointscalc})

print(players)