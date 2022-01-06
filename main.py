import csv

tournies = []
players = []
placements = ['1st', '2nd', '3rd', '4th', '5th', '7th', '9th']
points = { 1: {'1st': 15, '2nd': 13, '3rd': 10, '4th': 8, '5th': 7, '7th': 6, '9th': 5}, 2: {'1st': 10, '2nd': 8, '3rd': 7, '4th': 6, '5th': 5, '7th': 3, '9th': 2}, 3: {'1st': 5, '2nd': 4, '3rd': 3, '4th': 2, '5th': 1, '7th': 0, '9th': 0}, 4: {'1st': 4, '2nd': 3, '3rd': 2, '4th': 1, '5th': 0, '7th': 0, '9th': 0}, 5: {'1st': 1, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0, '7th': 0, '9th': 0} }

# populate tournaments dict
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        fifthlist = [row[10], row[11]]
        seventhlist = [row[12], row[13]]
        ninthlist = [row[14], row[15]]
        tournies.append({'id': row[0], 'date': row[1], 'name': row[2], 'link': row[3], 'entrants': row[4], 'tier': row[5], '1st': [row[6]], '2nd': [row[7]], '3rd': [row[8]], '4th': [row[9]], '5th': fifthlist, '7th': seventhlist, '9th': ninthlist})

# populate players dict 
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        for name in row[6:]:
            if name not in [x['name'] for x in players]:
                players.append({'name': name, 'placements': [], 'points': []})


# placements format:
# {
#   id:
#   place:
#   points:
# }


# sorting key for placements list of dicts
def sortPlacements(e):
    return e['points']

# sorting key for players based on points
def sortPlayers(e):
    if e['points']:
        return e['points'][-1][-1]
    else:
        return 0 # case for no points

# tourney placings for each player
for tourney in tournies:
    for place in placements:
        for player in players:
            if player['name'] in tourney[place]:
                pointscalc = points[int(tourney['tier'])][place]
                if pointscalc > 0:
                    tourneyid = tourney['id']
                    player['placements'].append({'id': tourneyid, 'place': place, 'points': pointscalc})
                    player['placements'].sort(reverse=True, key=sortPlacements)
                    # could make a list of lists of tourney id to points at the time for a future graph over time
                    pointslist = [l['points'] for l in player['placements']]
                    pointslist.reverse()
                    playerpoints = pointslist[0]
                    if len(pointslist) > 1:
                        for point in pointslist[1:]:
                            playerpoints *= .5 # exponential scaling
                            playerpoints += point
                    player['points'].append([tourneyid,playerpoints])

players.sort(reverse=True, key=sortPlayers)

print(players)

for player in players:
    if player['points']:
        print(player['name'] + ' ')
        print(str(player['points'][-1][-1]) + '\n')
    