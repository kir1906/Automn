from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class player(BaseModel):
    Name: str 
    bat_score: float 
    bow_score: float 
    all_bat: float
    all_bow: float
    wkt : float
    Oppsition : str
    Roll : str
    Team : str

# {
#   "Name": "Virat",
#   "bat_score": 2394.96,
#   "bow_score": 44.80,
#   "all_bat": 1680.95,
#   "all_bow": 1328.43,
#   "wkt": 1077.73,
#   "Oppsition": "South Africa",
#   "Roll": "Batsman",
#   "Team": "India"
# }


class finalist(BaseModel):
    team_matches: float
    team1_win: float
    team2_win: float
    team1_venue_matches: float
    team1_venue_win: float
    team2_venue_matches: float
    team2_venue_win: float
    team1_curr_match: float
    team1_curr_win: float
    team1_curr_perform: float
    team2_curr_match: float
    team2_curr_win: float
    team2_curr_perform: float
    team1_pre: str
    team2_pre: str
    venue_pre: str
    team1_win_to_lose: float
    team2_win_to_lose: float

# {
#   "team_matches": 44,
#   "team1_win": 21,
#   "team2_win": 22,
#   "team1_venue_matches": 93,
#   "team1_venue_win": 63,
#   "team2_venue_matches": 30,
#   "team2_venue_win": 14,
#   "team1_curr_match": 39,
#   "team1_curr_win": 26,
#   "team1_curr_perform": 66.67,
#   "team2_curr_match": 25,
#   "team2_curr_win": 15,
#   "team2_curr_perform": 60,
#   "team1_pre": "India",
#   "team2_pre": "Australia",
#   "venue_pre": "India",
#   "team1_win_to_lose": 1,
#   "team2_win_to_lose": 1
# }


class totalRun(BaseModel):
    Mat: float 
    Inns: float 
    Afghanistan: float 
    Australia: float
    Bangladesh: float
    England: float
    India: float
    Netherlands: float
    NewZealand: float 
    Pakistan: float
    SouthAfrica: float 
    SriLanka: float
    AVG_Run: float
    AVG_SR: float
    AVG_BF: float
    Player_pre: str
    Team_pre: str

# {
#   "Mat": 9,
#   "Inns": 9,
#   "Afghanistan": 1,
#   "Australia": 1,
#   "Bangladesh": 1,
#   "England": 1,
#   "India": 0,
#   "Netherlands": 1,
#   "NewZealand": 1,
#   "Pakistan": 1,
#   "SouthAfrica": 1,
#   "SriLanka": 1,
#   "AVG_Run": 78.92896559,
#   "AVG_SR": 87.43369524,
#   "AVG_BF": 0.202111361,
#   "Player_pre": "Virat Kohli",
#   "Team_pre": "india"
# }
