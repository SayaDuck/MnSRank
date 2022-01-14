import csv

tournies = []
players = []
placements = ['1st', '2nd', '3rd', '4th', '5th', '7th', '9th']

# Tourney tiers:
# 1 - Supermajor
# 2 - Major
# 3 - Stacked Weekly (or equivalent)
# 4 - Small Weekly (or equivalent)
# 5 - Beginner Tournament
points = { 1: {'1st': 15, '2nd': 12, '3rd': 10, '4th': 8, '5th': 7, '7th': 6, '9th': 5}, 2: {'1st': 10, '2nd': 8, '3rd': 7, '4th': 6, '5th': 5, '7th': 3, '9th': 2}, 3: {'1st': 5, '2nd': 4, '3rd': 3, '4th': 2, '5th': 1, '7th': 0, '9th': 0}, 4: {'1st': 4, '2nd': 3, '3rd': 2, '4th': 1, '5th': 0, '7th': 0, '9th': 0}, 5: {'1st': 1, '2nd': 0, '3rd': 0, '4th': 0, '5th': 0, '7th': 0, '9th': 0} }



# populate tournaments list
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        fifthlist = [row[10], row[11]]
        seventhlist = [row[12], row[13]]
        ninthlist = [row[14], row[15]]
        tournies.append({'id': row[0], 'date': row[1], 'name': row[2], 'link': row[3], 'entrants': row[4], 'tier': row[5], '1st': [row[6]], '2nd': [row[7]], '3rd': [row[8]], '4th': [row[9]], '5th': fifthlist, '7th': seventhlist, '9th': ninthlist})

# populate players list
with open('data/MnS_2021_Tournaments.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        for name in row[6:]:
            if name not in [x['name'] for x in players]:
                if name: # check for empty
                    players.append({'name': name, 'placements': [], 'points': []})

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

                # placement only counted if it's worth something
                if pointscalc > 0:
                    tourneyid = tourney['id']
                    player['placements'].append({'id': tourneyid, 'place': place, 'points': pointscalc})
                    
                    # sorts placements from most valuable to least
                    player['placements'].sort(reverse=True, key=sortPlacements) 
                    
                    # list of placements, which is then flipped so worst is first
                    pointslist = [l['points'] for l in player['placements']]
                    pointslist.reverse()

                    # worst placement initial
                    playerpoints = pointslist[0]
                    if len(pointslist) > 1:
                        for point in pointslist[1:]:
                            playerpoints *= .5 # exponential scaling
                            playerpoints += point
                    
                    # adds to point history (adds every time for a historical progression over tournaments)
                    player['points'].append([tourneyid,playerpoints])

# sorts players from most points to least
players.sort(reverse=True, key=sortPlayers)

# so the top player gets 100
scalefactor = 100/players[0]['points'][-1][-1]

# loops through and scales so final result of #1 is 100
for player in players:
    for result in player['points']:
        result[-1] *= scalefactor

# prints players and then their points (if >0)
for player in players:
    if player['points']:
        print(player['name'] + ' ' + str(round(player['points'][-1][-1], 2)))


# player info dict
playerinfo = {}

# populate player info dict
with open('data/MnS_2021_PlayerInfo.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        playerinfo[row[0]] = {'name': row[0], 'main': row[1].split(), 'secondary': row[2].split(), 'input': row[3], 'country': row[4], 'twitter': row[5], 'youtube': row[6], 'twitch': row[7], 'firsttourney': row[8], 'pronouns': row[10], 'blurb': row[11]}


# uses the index jinja template to generate a page
import page
page.generate("MnSRank 2021", tournies, players, playerinfo)