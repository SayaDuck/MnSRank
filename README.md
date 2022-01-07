# MnSRank
Maiden &amp; Spell community player ranking based on tournament data.

## Why?
2021 just ended and this seemed like a cool idea. Elo doesn't work well for various reasons that all apply to MnS (small community, low volume of tourney games, double elimination). Making a ranking that was purely how well someone did in tournaments this year (**not** how "skilled" they are) was the goal.

## Methodology
All Maiden & Spell tournament data of the year was compiled, along with the top 12 placers at each tournament. For a tournament to qualify, it must be a double-elimination tournament with the standard ruleset. 

This data was then processed to generate a list of player dictionaries, which were then filled with that player's placements. Looping through those placements per player, points were assigned to each placement depending on the tier of the tournament and the placement itself. The points were then added and scaled (exponential decay w/ halving, so your best performance counts most and so attending everything doesn't give you a massive amount of points). An entry was added to a player's points list every time a placement was added to a player, allowing for a visualization of how points increased over the year (and from specific tournaments). After one last round of sorting, the top player's final point total is found and used to scale all points so that the #1 player ends with a 100.
## The Ranking
### MnSRank 2021 Rev. 1
| Player        | Score |
|---------------|-------|
| iLLy          | 100.0 |
| nix           | 72.03 |
| Centispede    | 51.63 |
| Jayfeather6   | 50.76 |
| Xorn          | 49.01 |
| A1NVERSE      | 47.47 |
| Maven         | 46.59 |
| frog          | 46.59 |
| Quetzalcoatl  | 44.4  |
| kerokero      | 42.77 |
| minkull       | 42.2  |
| Jahvaro       | 41.32 |
| Kiroko        | 40.44 |
| ZaleTheBale   | 38.68 |
| 木天明        | 36.92 |
| rem           | 33.85 |
| Hourai        | 29.75 |
| auxzilla      | 29.23 |
| Winter        | 26.59 |
| Kewpie_Kewpie | 25.06 |
| Ueomia        | 24.62 |
| Meguca        | 24.39 |
| rei           | 21.1  |
| HoboDessert   | 21.04 |
| Pug           | 20.19 |
| Tastyfood     | 17.58 |
| glitch        | 14.07 |
| Saki          | 10.55 |
| Shadowpelt721 | 9.67  |
| peteru        | 8.79  |
| Dino          | 7.03  |
| Hydroclopse   | 7.03  |
| games         | 7.03  |
| blasterthefox | 6.59  |
| bubbles_71    | 5.27  |
| Airvent       | 3.52  |
| qwwert        | 3.52  |
| Atchinson     | 3.52  |
| TruXai        | 3.52  |
| yllt          | 3.52  |
| gameringering | 3.52  |

## Soon...
- Automatically generated infographics per player with graphs and most valuable placements
