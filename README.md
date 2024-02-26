### Points (PointByPoint) Description

#### **match_id**
- **Description**: Unique ID for the match.
- **Example**: `2023-wimbledon-1101`

#### **ElapsedTime**
- **Description**: Clock time elapsed since the match began.
- **Example**: `0:32:15` (32 minutes and 15 seconds)

#### **SetNo**
- **Description**: Current set number.
- **Example**: `2`

#### **P1GamesWon**
- **Description**: Number of games won by Player 1 in the current set.
- **Example**: `3`

#### **P2GamesWon**
- **Description**: Number of games won by Player 2 in the current set.
- **Example**: `4`

#### **SetWinner**
- **Description**: Player number of the set winner; `0` if the set is ongoing.
- **Values**: `0` (ongoing), `1` (Player 1), `2` (Player 2)

#### **GameNo**
- **Description**: The ongoing game number within the set.
- **Example**: `7`

#### **GameWinner**
- **Description**: Player number of the game winner; `0` if the game is ongoing.
- **Values**: `0` (ongoing), `1` (Player 1), `2` (Player 2)

#### **PointNumber**
- **Description**: Unique identifier for each point within the match.
- **Example**: `15` (15th point of the match)

#### **PointWinner**
- **Description**: Player number who won the point.
- **Values**: `1` (Player 1), `2` (Player 2)

#### **PointServer**
- **Description**: Player number serving the point.
- **Values**: `1` (Player 1), `2` (Player 2)

#### Serve and Point Details

#### **Speed_KMH**
- **Description**: Speed of the serve in kilometers per hour.
- **Example**: `185` (indicating a fast serve)

#### **Rally**
- **Description**: The sequence of shots in the point. This could be a numerical value indicating the length of the rally.
- **Example**: `4` (indicating a 4-shot rally)

#### **P1Score**, **P2Score**
- **Description**: Current game score from the perspective of each player, typically not numerical but represented in traditional tennis scoring terms.
- **Example**: P1Score: `15`, P2Score: `30`

#### **P1Momentum**, **P2Momentum**
- **Description**: Momentum indicator for each player, potentially quantifying aspects like consecutive points won.
- **Example**: P1Momentum: `2`, P2Momentum: `0` (Player 1 has won 2 points in a row)

#### **P1PointsWon**, **P2PointsWon**
- **Description**: Total points won by each player in the match.
- **Example**: P1PointsWon: `45`, P2PointsWon: `42`

#### **P1Ace**, **P2Ace**
- **Description**: Total aces served by each player in the match.
- **Example**: P1Ace: `3`, P2Ace: `1`

#### **P1Winner**, **P2Winner**
- **Description**: Total winners hit by each player.
- **Example**: P1Winner: `12`, P2Winner: `8`

#### **P1DoubleFault**, **P2DoubleFault**
- **Description**: Total double faults served by each player.
- **Example**: P1DoubleFault: `2`, P2DoubleFault: `1`

#### **P1UnfErr**, **P2UnfErr**
- **Description**: Total unforced errors made by each player.
- **Example**: P1UnfErr: `10`, P2UnfErr: `8`

#### **P1NetPoint**, **P2NetPoint**
- **Description**: Total net points played by each player.
- **Example**: P1NetPoint: `5`, P2NetPoint: `4`

#### **P1NetPointWon**, **P2NetPointWon**
- **Description**: Total net points won by each player.
- **Example**: P1NetPointWon: `3`, P2NetPointWon: `2`

#### **P1BreakPoint**, **P2BreakPoint**
- **Description**: Total break points faced by each player.
- **Example**: P1BreakPoint: `4`, P2BreakPoint: `3`

#### **P1BreakPointWon**, **P2BreakPointWon**
- **Description**: Total break points won by each player.
- **Example**: P1BreakPointWon: `2`, P2BreakPointWon: `1`

#### **P1FirstSrvIn**, **P2FirstSrvIn**
- **Description**: Total first serves in by each player.
- **Example**: P1FirstSrvIn: `30`, P2FirstSrvIn: `28`

#### **P1FirstSrvWon**, **P2FirstSrvWon**
- **Description**: Total first serve points won by each player.
- **Example**: P1FirstSrvWon: `24`, P2FirstSrvWon: `20`

#### **P1SecondSrvIn**, **P2SecondSrvIn**
- **Description**: Total second serves in by each player.
- **Example**: P1SecondSrvIn: `15`, P2SecondSrvIn: `14`

#### **P1SecondSrvWon**, **P2SecondSrvWon**
- **Description**: Total second serve points won by each player.
- **Example**: P1SecondSrvWon: `8`, P2SecondSrvWon: `7`

#### **P1ForcedError**, **P2ForcedError**
- **Description**: Total forced errors made by each player.
- **Example**: P1ForcedError: `6`, P2ForcedError: `5`

#### Additional Metrics and Context

#### **History**
- **Description**: Historical performance or head-to-head stats until that point. Might be numerical or categorical.
- **Example**: `Player 1 leads 2-1 in previous meetings`

#### **Speed_MPH**
- **Description**: Speed of the serve in miles per hour.
- **Example**: `115` (alternative measurement for serve speed)

#### **P1BreakPointMissed**, **P2BreakPointMissed**
- **Description**: Total break points not converted by each player.
- **Example**: P1BreakPointMissed: `2`, P2BreakPointMissed: `2`

#### **ServeIndicator**
- **Description**: Distinguishes between the first and second serves.
- **Values**: `1` (First Serve), `2` (Second Serve)

#### **Serve_Direction**
- **Description**: Direction of the serve (e.g., wide, body, T).
- **Values**: `Wide`, `Body`, `T`

#### **Winner_FH**, **Winner_BH**
- **Description**: Indicator of whether a winner was a forehand or backhand.
- **Values**: `FH` (Forehand Winner), `BH` (Backhand Winner)

#### **ServingTo**
- **Description**: The side of the receiver the serve is directed to.
- **Values**: `Deuce`, `Ad` (Advantage)

#### **P1TurningPoint**, **P2TurningPoint**
- **Description**: Indicator of a turning point in momentum or psychological advantage.
- **Values**: Binary indicator, `1` if a turning point was identified, otherwise `0`.

#### **ServeNumber**
- **Description**: Distinguishes between first and second serve attempts within a point.
- **Values**: `1`, `2`

#### **WinnerType**
- **Description**: Category of shot that won the point.
- **Values**: Various types such as `Ace`, `Winner`, `Forced Error`

#### **WinnerShotType**
- **Description**: Specific shot type that won the point (e.g., forehand, backhand, volley).
- **Values**: `Forehand`, `Backhand`, `Volley`

#### **P1DistanceRun**, **P2DistanceRun**
- **Description**: Distance run by each player during the point, in meters.
- **Example**: P1DistanceRun: `20`, P2DistanceRun: `18`

#### **RallyCount**
- **Description**: Number of shots exchanged in the rally.
- **Example**: `5`

#### ServeWidth
- **Description**: Location of the serve.
- **Values**:
- `B`: Body
- `BC`: Body/Center
- `BW`: Body/Wide
- `C`: Center (down the T)
- `W`: Wide

#### ServeDepth
- **Description**: Depth of the serve.
- **Values**:
- `CTL`: Close To Line
- `NCTL`: Not Close To Line

#### ReturnDepth
- **Description**: Depth of the return.
- **Values**:
- `D`: Deep
- `ND`: Not Deep


### Matches Dataset Description

#### Tournament and Match Identification

- **match_id**
    - **Description**: Unique identifier for each match.
    - **Example**: `2023-wimbledon-1101`
- **year**
    - **Description**: The year the match took place.
    - **Example**: `2023`
- **slam**
    - **Description**: The name of the Grand Slam tournament.
    - **Example**: `Wimbledon`
- **match_num**
    - **Description**: A unique number assigned to each match within the tournament.
    - **Example**: `1101`

#### Player Information

- **player1**
    - **Description**: Name of the first player or Player 1.
    - **Example**: `Novak Djokovic`
- **player2**
    - **Description**: Name of the second player or Player 2.
    - **Example**: `Roger Federer`
- **player1id**
    - **Description**: Unique identifier for Player 1.
    - **Example**: `104925` (This is an example; actual IDs will vary.)
- **player2id**
    - **Description**: Unique identifier for Player 2.
    - **Example**: `103819` (This is an example; actual IDs will vary.)

#### Match Outcome

- **status**
    - **Description**: Status of the match (e.g., completed, in progress).
    - **Values**: `Completed`, `In Progress`
- **winner**
    - **Description**: Identifier for the match winner (corresponds to `player1` or `player2`).
    - **Values**: `1` (Player 1), `2` (Player 2)

#### Tournament Context

- **event_name**
    - **Description**: The specific event within the tournament (e.g., Men's Singles, Women's Singles).
    - **Example**: `Men's Singles`
- **round**
    - **Description**: The round of the tournament in which the match took place (e.g., Final, Semi-finals).
    - **Values**: `Final`, `Semi-finals`, `Quarter-finals`, etc.

#### Venue Details

- **court_name**
    - **Description**: The name of the court where the match was played.
    - **Example**: `Centre Court`
- **court_id**
    - **Description**: Unique identifier for the court.
    - **Example**: `1` (This is an example; actual IDs will vary.)

#### Player Nationality

- **nation1**
    - **Description**: Nationality of Player 1.
    - **Example**: `SRB` (for Serbia)
- **nation2**
    - **Description**: Nationality of Player 2.
    - **Example**: `SUI` (for Switzerland)