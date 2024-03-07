# Useful Available Datasets

## Jeffsackmann's tennis abstract data: https://tennisabstract.com

- ### [Tennis_atp](https://github.com/JeffSackmann/tennis_atp)
  - `Dictionary`: [tennis_atp matches_data_dictionary](https://github.com/JeffSackmann/tennis_atp/blob/master/matches_data_dictionary.txt)

- ### [Tennis_wta](https://github.com/JeffSackmann/tennis_wta)
  - `Dictionary`(Same as atp): [tennis_atp matches_data_dictionary](https://github.com/JeffSackmann/tennis_atp/blob/master/matches_data_dictionary.txt)
- ### [Tennis_MatchChartingProject](https://github.com/JeffSackmann/tennis_MatchChartingProject)

  - `Dictionary`: [MatchChartingProject data_dictionary](https://github.com/JeffSackmann/tennis_MatchChartingProject/blob/master/data_dictionary.txt)


- ### [Tennis_slam_pointbypoint](https://github.com/JeffSackmann/tennis_slam_pointbypoint)

  - #### `Dictionary / Description`:
    - [Points dataset](#Points-dataset)
  
      - [General Match Information](#General-Match-Information)
      - [Serve and Point Details](#Serve-and-Point-Details)
      - [Additional Metrics and Context](#Additional-Metrics-and-Context)
  
    - [Matches datasets](#Matches-datasets)
  
      - [Tournament and Match Identification](#Tournament-and-Match-Identification)
      - [Player Information](#Player-Information)
      - [Match Outcome](#Match-Outcome)
      - [Tournament Context](#Tournament-Context)
      - [Venue Details](#Venue-Details)
      - [Player Nationality](#Player-Nationality)
  
    - [Missing data](#Missing-data)


## Infosys Australian Open & Roland Garros 'scraped' data: [Hawkeye scrap reference](https://github.com/ryurko/hawkeye)

  - `Dictionary`: [Courtvision data_dictionary](#CourtVision-Data)
  - AO Open match example: [Sinner vs medvedev AO Open Final match page](https://ausopen.com/match/2024-jannik-sinner-vs-daniil-medvedev-ms701#!infosys-3)

AO Open and RG oficial data (and possibily other Infosys managed tournaments), is available in their website
This data is generally high quality since it provides a interface for samples of ['Hawkeye' Data](#CourtVision-Data)
However, this data had to be 'scraped' since their API is encrypted.
So this data is `public` but initially unaccessible.

Since all the matches general info (Ex. Match id, Players id, Points id) is already available: By decrypting their API responses, meaning getting a proper JSON), its possible to iterate through the matches using match info to get point by point data for each match.

These [Jeffsackmann tennis_slam_pointbypoint](https://github.com/JeffSackmann/tennis_slam_pointbypoint) datasets are incomplete mostly because they lack this kind of 'unaccessible' data

> [!IMPORTANT]
> In the past, individuals successfully leveraged this API to create datasets: [Hawkeye scrap](https://github.com/ryurko/hawkeye) by dumping the JSON responses and converting them to a proper csv, however since the changes made to the Infosys API, the JSON dumping step of these scraping methods no longer work, nonetheless, now its possible to reverse engineer how their frontend processes the new encrypted API response by using the decode function from [API_Decryption Example](https://github.com/hawkilol/TennisCC/blob/main/AO_scrap_API.py) to translate it to proper JSON: [AO Open Match JSON dump](https://github.com/hawkilol/TennisCC/blob/main/atp_AO_Open_year_2024_MS101_tracking_data.json) , thus enabling their script to create fresh datasets once again 😎 : [Play By Play Example csv](https://github.com/hawkilol/TennisCC/blob/main/atp_australian_open_2024_MS101_pbp.csv) and [Ball Tracking example csv](https://github.com/hawkilol/TennisCC/blob/main/atp_australian_open_2024_MS101_ball_trajectory.csv) for more info see [Play By Play Description](#Play-by-Play) and [Ball Tracking Description](#Ball-Tracking-(rally)) respectively


- ! After the initial decryption, the values are intact but the property names are weird, but consistent, so by using the diff between it and a original JSON
  it can be mapped to the correct names
  

### CourtVision Data

CourtVision data, contains data that can only be obtained by high quality on court sensor like the Hawkeye system such as ball coordinates and speed... 
see the [Sinner vs medvedev AO Open Final match page](https://ausopen.com/match/2024-jannik-sinner-vs-daniil-medvedev-ms701#!infosys-3) and select CourtVision for visual reference

#### Play by Play
Each .csv file chronicles the outcomes of all points in the match, !lacking data on let points!, and includes information on ball trajectories, such as serve impacts and bounces, and serve-return interactions.

  * `point_ID`: Character point ID
  * `set_num`: Set Number
  * `game_num`: Game Number
  * `point_num`: Point number WITHIN a game (always starts at 1)
  * `serve_num`: Serve Number (1,2). Lets are not tracked.
  * `server_id`: 'Server ID
  * `returner_id`: Returner ID
  * `point_winner_id`: Point Winner ID (either serverID or returnerID)
  * `court_side`: Serve Court ('AdCourt' or 'DeuceCourt')
  * `serve_speed_kph`: Serve Speed in Kilometers per Hour
  * `serve_type`:'Flat', 'Pronated', 'Slice', 'Unclassified'
  * `fault_distance_missed_m`: If serve was fault, by how much did it miss? In Metres
  * `(x,y,z)_ball_serve_impact`: Location of where the serve ball was struck.
  * `rally_length`: Length of rally (including serve)
  * `point_end_type`: How did rally end? Ex: Fault, Unforced/Forced error, Winner
  * `error_type`: If point ended in an error, which type? Ex: Net, Wide, Long
  * `trapped_by_net`: *I think* Boolean for whether shot was net error?
  * `slast_troke`: Type of stroke on last shot of rally. Ex: Ground, Passing, Drop. "Last shot" means any last recorded shot (winner, error, etc)
  * `last_hand`: Handedness on last shot.
  * `last_stroke_net_height_m`: Ball height at net on last shot of rally (in metres).
  * `winner_placement`: Cross Court or Down the Line
  * `unforcedErrorPlacement`: If shot error, what type? Wide, Net, Long. This is the same as `error_type`?
  * `is_break_point`: Boolean
  * `is_break_point_converted`: Boolean
  * `runAroundForeHand`: Boolean
  * `is_track_avail`: Boolean. Indicates whether ball tracking data is available for this rally sequence. 
  * `(x,y,z)_serve_bounce`: coordinates of serve bounce
  * `serve_dir`: Serve Direction (T, Wide, Body)
  * `(x,y,z)_net_serve`: coordinates of serve ball as it reached the net
  * `last_ball_impact_(x,y,z)`: Coordinates of last location ball was hit
  * `last_ball_bounce_(x,y,z)`: coordinates of last ball bounce
  * `serve_return_impact_(x,y,z)`: coordinates of where the returner made contact with serve
  * `serve_return_net_(x,y,z)`: coordinates of where the serve-return shot reached the net
  * `serve_return_bounce_(x,y,z)`: coordinates of where the serve-return shot landed
  * `spin_rpm`: Ball spin on last rally shot
  * `is_fault`: 0 = Not fault; 1= Fault 
  * `is_doublefault`: 0 = Not doublefault; 1= doublefault 
  * `is_tiebreak`: Indicator for current point being a tiebreak
  * `is_ace`: Indicator if serve is an ace
  * `is_prev_doublefault`: Indicator if serve is doublefault
  * `is_prev_ace`: Indicator if previous serve was an ace
  <!--
  * `server_score`: 
  * `returner_score`:
  * `player1`:
  * `player2`:
  * `p1_cum_games`:
  * `p2_cum_games`:
  * `p1_cum_sets`:
  * `p2_cum_sets`:
  -->

#### Ball Tracking (rally)

Each .csv file holds the trajectory details of the ball for every rally of a match, the (x,y,z) coordinates of the ball are only registered in specific moments: when the ball is struck (hit), at its apex (peak), as it approaches the net (net), and when it makes contact with the ground (bounce).

  * `point_ID`: Character point ID
  * `set_num`: Set Number
  * `game_num`: Game Number
  * `point_num`: Point number WITHIN a game (always starts at 1)
  * `serve_num`: Serve Number (1,2). Lets are not tracked.
  * `strike_index`: Count for ball being hit by a player in the rally
  * `position`: Position the ball is struck (hit), at its apex (peak), as it approaches the net (net), and when it makes contact with the ground (bounce)
  * `(x,y,z)`: Ball location when a position event happens
  
<!---### Summary -->



-------------------------------------------------------- End here -------------------------------------------------------------
## Tennis_slam_pointbypoint
### Points dataset
(Point by point)
#### General Match Information

- `match_id`

  - `Description`: Unique ID for the match.
  - `Example`: `2023-wimbledon-1101`

- `ElapsedTime`

  - `Description`: Clock time elapsed since the match began.
  - `Example`: `0:32:15` (32 minutes and 15 seconds)

- `SetNo`

  - `Description`: Current set number.
  - `Example`: `2`

- `P1GamesWon`

  - `Description`: Number of games won by Player 1 in the current set.
  - `Example`: `3`

- `P2GamesWon`

  - `Description`: Number of games won by Player 2 in the current set.
  - `Example`: `4`

- `SetWinner`

  - `Description`: Player number of the set winner; `0` if the set is ongoing.
  - `Values`: `0` (ongoing), `1` (Player 1), `2` (Player 2)

- `GameNo`

  - `Description`: The ongoing game number within the set.
  - `Example`: `7`

- `GameWinner`

  - `Description`: Player number of the game winner; `0` if the game is ongoing.
  - `Values`: `0` (ongoing), `1` (Player 1), `2` (Player 2)

- `PointNumber`

  - `Description`: Unique identifier for each point within the match.
  - `Example`: `15` (15th point of the match)

- `PointWinner`

  - `Description`: Player number who won the point.
  - `Values`: `1` (Player 1), `2` (Player 2)

- `PointServer`
  - `Description`: Player number serving the point.
  - `Values`: `1` (Player 1), `2` (Player 2)

#### Serve and Point Details

- `Speed_KMH`

  - `Description`: Speed of the serve in kilometers per hour.
  - `Example`: `185` (indicating a fast serve)

- `Rally`

  - `Description`: The sequence of shots in the point. This could be a numerical value indicating the length of the rally.
  - `Example`: `4` (indicating a 4-shot rally)

- `P1Score`, `P2Score`

  - `Description`: Current game score from the perspective of each player, typically not numerical but represented in traditional tennis scoring terms.
  - `Example`: P1Score: `15`, P2Score: `30`

- `P1Momentum`, `P2Momentum`

  - `Description`: Momentum indicator for each player, potentially quantifying aspects like consecutive points won.
  - `Example`: P1Momentum: `2`, P2Momentum: `0` (Player 1 has won 2 points in a row)

- `P1PointsWon`, `P2PointsWon`

  - `Description`: Total points won by each player in the match.
  - `Example`: P1PointsWon: `45`, P2PointsWon: `42`

- `P1Ace`, `P2Ace`

  - `Description`: Total aces served by each player in the match.
  - `Example`: P1Ace: `3`, P2Ace: `1`

- `P1Winner`, `P2Winner`

  - `Description`: Total winners hit by each player.
  - `Example`: P1Winner: `12`, P2Winner: `8`

- `P1DoubleFault`, `P2DoubleFault`

  - `Description`: Total double faults served by each player.
  - `Example`: P1DoubleFault: `2`, P2DoubleFault: `1`

- `P1UnfErr`, `P2UnfErr`

  - `Description`: Total unforced errors made by each player.
  - `Example`: P1UnfErr: `10`, P2UnfErr: `8`

- `P1NetPoint`, `P2NetPoint`

  - `Description`: Total net points played by each player.
  - `Example`: P1NetPoint: `5`, P2NetPoint: `4`

- `P1NetPointWon`, `P2NetPointWon`

  - `Description`: Total net points won by each player.
  - `Example`: P1NetPointWon: `3`, P2NetPointWon: `2`

- `P1BreakPoint`, `P2BreakPoint`

  - `Description`: Total break points faced by each player.
  - `Example`: P1BreakPoint: `4`, P2BreakPoint: `3`

- `P1BreakPointWon`, `P2BreakPointWon`

  - `Description`: Total break points won by each player.
  - `Example`: P1BreakPointWon: `2`, P2BreakPointWon: `1`

- `P1FirstSrvIn`, `P2FirstSrvIn`

  - `Description`: Total first serves in by each player.
  - `Example`: P1FirstSrvIn: `30`, P2FirstSrvIn: `28`

- `P1FirstSrvWon`, `P2FirstSrvWon`

  - `Description`: Total first serve points won by each player.
  - `Example`: P1FirstSrvWon: `24`, P2FirstSrvWon: `20`

- `P1SecondSrvIn`, `P2SecondSrvIn`

  - `Description`: Total second serves in by each player.
  - `Example`: P1SecondSrvIn: `15`, P2SecondSrvIn: `14`

- `P1SecondSrvWon`, `P2SecondSrvWon`

  - `Description`: Total second serve points won by each player.
  - `Example`: P1SecondSrvWon: `8`, P2SecondSrvWon: `7`

- `P1ForcedError`, `P2ForcedError`
  - `Description`: Total forced errors made by each player.
  - `Example`: P1ForcedError: `6`, P2ForcedError: `5`

#### Additional Metrics and Context

- `History`

  - `Description`: Historical performance or head-to-head stats until that point. Might be numerical or categorical.
  - `Example`: `Player 1 leads 2-1 in previous meetings`

- `Speed_MPH`

  - `Description`: Speed of the serve in miles per hour.
  - `Example`: `115` (alternative measurement for serve speed)

- `P1BreakPointMissed`, `P2BreakPointMissed`

  - `Description`: Total break points not converted by each player.
  - `Example`: P1BreakPointMissed: `2`, P2BreakPointMissed: `2`

- `ServeIndicator`

  - `Description`: Distinguishes between the first and second serves.
  - `Values`: `1` (First Serve), `2` (Second Serve)

- `Serve_Direction`

  - `Description`: Direction of the serve (e.g., wide, body, T).
  - `Values`: `Wide`, `Body`, `T`

- `Winner_FH`, `Winner_BH`

  - `Description`: Indicator of whether a winner was a forehand or backhand.
  - `Values`: `FH` (Forehand Winner), `BH` (Backhand Winner)

- `ServingTo`

  - `Description`: The side of the receiver the serve is directed to.
  - `Values`: `Deuce`, `Ad` (Advantage)

- `P1TurningPoint`, `P2TurningPoint`

  - `Description`: Indicator of a turning point in momentum or psychological advantage.
  - `Values`: Binary indicator, `1` if a turning point was identified, otherwise `0`.

- `ServeNumber`

  - `Description`: Distinguishes between first and second serve attempts within a point.
  - `Values`: `1`, `2`

- `WinnerType`

  - `Description`: Category of shot that won the point.
  - `Values`: Various types such as `Ace`, `Winner`, `Forced Error`

- `WinnerShotType`

  - `Description`: Specific shot type that won the point (e.g., forehand, backhand, volley).
  - `Values`: `Forehand`, `Backhand`, `Volley`

- `P1DistanceRun`, `P2DistanceRun`

  - `Description`: Distance run by each player during the point, in meters.
  - `Example`: P1DistanceRun: `20`, P2DistanceRun: `18`

- `RallyCount`

  - `Description`: Number of shots exchanged in the rally.
  - `Example`: `5`

- `ServeWidth`

  - `Description`: Location of the serve relative to the court width (e.g., Wide, Body, Center).
  - `Values`: `Wide`, `Body`, `Center`

- `ServeDepth`

  - `Description`: Depth of the serve (e.g., Close To Line, Not Close To Line).
  - `Values`: `CTL` (Close To Line), `NCTL` (Not Close To Line)

- `ReturnDepth`
  - `Description`: Depth of the return (e.g., Deep, Not Deep).
  - `Values`: `Deep`, `Not Deep`

### Matches datasets

#### Tournament and Match Identification

- `match_id`
  - `Description`: Unique identifier for each match.
  - `Example`: `2023-wimbledon-1101`
- `year`
  - `Description`: The year the match took place.
  - `Example`: `2023`
- `slam`
  - `Description`: The name of the Grand Slam tournament.
  - `Example`: `Wimbledon`
- `match_num`
  - `Description`: A unique number assigned to each match within the tournament.
  - `Example`: `1101`

#### Player Information

- `player1`
  - `Description`: Name of the first player or Player 1.
  - `Example`: `Novak Djokovic`
- `player2`
  - `Description`: Name of the second player or Player 2.
  - `Example`: `Roger Federer`
- `player1id`
  - `Description`: Unique identifier for Player 1.
  - `Example`: `104925` (This is an example; actual IDs will vary.)
- `player2id`
  - `Description`: Unique identifier for Player 2.
  - `Example`: `103819` (This is an example; actual IDs will vary.)

#### Match Outcome

- `status`
  - `Description`: Status of the match (e.g., completed, in progress).
  - `Values`: `Completed`, `In Progress`
- `winner`
  - `Description`: Identifier for the match winner (corresponds to `player1` or `player2`).
  - `Values`: `1` (Player 1), `2` (Player 2)

#### Tournament Context

- `event_name`
  - `Description`: The specific event within the tournament (e.g., Men's Singles, Women's Singles).
  - `Example`: `Men's Singles`
- `round`
  - `Description`: The round of the tournament in which the match took place (e.g., Final, Semi-finals).
  - `Values`: `Final`, `Semi-finals`, `Quarter-finals`, etc.

#### Venue Details

- `court_name`
  - `Description`: The name of the court where the match was played.
  - `Example`: `Centre Court`
- `court_id`
  - `Description`: Unique identifier for the court.
  - `Example`: `1` (This is an example; actual IDs will vary.)

#### Player Nationality

- `nation1`
  - `Description`: Nationality of Player 1.
  - `Example`: `SRB` (for Serbia)
- `nation2`
  - `Description`: Nationality of Player 2.
  - `Example`: `SUI` (for Switzerland)

#### Missing data

[['Missing' events]]
['Missing' Events](https://github.com/JeffSackmann/tennis_slam_pointbypoint?tab=readme-ov-file#missing-events)
