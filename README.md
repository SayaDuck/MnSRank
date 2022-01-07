# MnSRank
Maiden &amp; Spell community player ranking based on tournament data.

## Why?
2021 just ended and this seemed like a cool idea. Elo doesn't work well for various reasons that all apply to MnS (small community, low volume of tourney games, double elimination). Making a ranking that was purely how well someone did in tournaments this year (NOT how "skilled" they are) was the goal.

## Methodology
All Maiden & Spell tournament data of the year was compiled, along with the top 12 placers at each tournament. For a tournament to qualify, it must be a double-elimination tournament with the standard ruleset. 

This data was then processed to generate a list of player dictionaries, which were then filled with that player's placements. Looping through those placements per player, points were assigned to each placement depending on the tier of the tournament and the placement itself. The points were then added and scaled (exponential decay w/ halving, so your best performance counts most and you can't farm).
## The Ranking
### MnSRank 2021 Rev. 1
| Player        | Score              |
|---------------|--------------------|
| iLLy          | 28.43737018108368  |
| nix           | 21.984130859375    |
| Centispede    | 14.683073997497559 |
| Jayfeather6   | 14.43530023097992  |
| Xorn          | 13.9375            |
| A1NVERSE      | 13.5               |
| Maven         | 13.25              |
| frog          | 13.25              |
| minkull       | 13                 |
| Quetzalcoatl  | 12.625             |
| kerokero      | 12.163818359375    |
| Jahvaro       | 11.75              |
| Kiroko        | 11.5               |
| ZaleTheBale   | 11.0               |
| 木天明        | 10.5               |
| rem           | 9.625              |
| Hourai        | 8.4609375          |
| auxzilla      | 8.3125             |
| Winter        | 7.5625             |
| Kewpie_Kewpie | 7.125              |
| Ueomia        | 7                  |
| Meguca        | 6.935546875        |
| rei           | 6                  |
| HoboDessert   | 5.9833831787109375 |
| Pug           | 5.74169921875      |
| Tastyfood     | 5                  |
| glitch        | 4.0                |
| Saki          | 3                  |
| Shadowpelt721 | 2.75               |
| peteru        | 2.5                |
| Dino          | 2                  |
| Hydroclopse   | 2                  |
| games         | 2                  |
| blasterthefox | 1.875              |
| bubbles_71    | 1.5                |
| Airvent       | 1                  |
| qwwert        | 1                  |
| Atchinson     | 1                  |
| TruXai        | 1                  |
| yllt          | 1                  |
| gameringering | 1                  |