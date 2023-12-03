#import library
import uvicorn
from flask import Flask, render_template, request
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from p3 import player,totalRun,finalist
import numpy as np
import pickle
import pandas as pd
import tensorflow
import keras
#create the app object
most_fours_model = keras.models.load_model('most_fours.h5')
finalists_model = keras.models.load_model('finalist.h5')
total_run_model = keras.models.load_model('total_run_prediction.h5')
app=FastAPI()
templates = Jinja2Templates(directory="templates")
pickle_mod = open('player.pkl', 'rb')
model,standard = pickle.load(pickle_mod)
pickle_mod.close()
pickle_mo = open('finalist.pkl', 'rb')
standard_1 = pickle.load(pickle_mo)
pickle_m = open('most_fours.pkl', 'rb')
standard_2 = pickle.load(pickle_m)

def co(data,standard_scaler):
  ordinal_team = {'Australia': 0, 'South Africa': 1, 'Sri Lanka': 2,'England':3,'New Zealand':4,'Bangladesh':5,'Pakistan':6,'Afghanistan':7\
                   ,'India':8,'Netherlands':9}
  ordinal_player = {'Abdul Rahman': 0,
 'Abdullah Shafique': 1,
 'Adam Zampa': 2,
 'Adil_Usman_Rashid': 3,
 'Aiden Markram': 4,
 'Alex Carey': 5,
 'Andile Phehlukwayo': 6,
 'Angelo Mathews': 7,
 'Angus_Alexander_Patrick_Atkinson': 8,
 'Anil Teja Nidamanuru': 9,
 'Aryan Dutt': 10,
 'Axar Pate': 11,
 'Azmatullah Omarzai': 12,
 'Bas de Leede': 13,
 'Benjamin_Andrew_Stokes': 14,
 'Brydon_Alexander_Carse': 15,
 'Cameron Green': 16,
 'Chamika Karunaratne': 17,
 'Charith Asalanka': 18,
 'Christopher_Roger_Woakes': 19,
 'Colin Niel Ackermann': 20,
 'Darly Mitchell': 21,
 'Dasun Shanaka': 22,
 'David Miller': 23,
 'David Warner': 24,
 'David_Jonathan_Willey': 25,
 'Dawid_Johannes_Malan': 26,
 'Devon Conway': 27,
 'Dhananjaya de Silva': 28,
 'Dilshan Madushanka': 29,
 'Dimuth Karunaratne': 30,
 'Dunith Wellalage': 31,
 'Dushan Hemantha': 32,
 'Dushmantha Chameera': 33,
 'Fakhar Zaman': 34,
 'Fazalhaq Farooqi': 35,
 'Gerald Coetzee': 36,
 'Glenn Maxwell': 37,
 'Glenn Phillips': 38,
 'Hardik Pandya': 39,
 'Haris Rauf': 40,
 'Harry_Cherrington_Brook': 41,
 'Hasan Ali': 42,
 'Hasan Mahmud': 43,
 'Hashmatullah Shahidi': 44,
 'Heinrich Klaasen': 45,
 'Ibrahim Zadran': 46,
 'Iftikhar Ahmed': 47,
 'Ikram Alikhil': 48,
 'Imam-ul-Haq': 49,
 'Ish Sodhi': 50,
 'Ishan Kishan': 51,
 'Jasprit Bumrah': 52,
 'Jonathan_Marc_Bairstow': 53,
 'Joseph Charles Buttler': 54,
 'Joseph_Edward_Root': 55,
 'Josh Hazlewood': 56,
 'Josh Inglis': 57,
 'KL Rahul': 58,
 'Kagiso Rabada': 59,
 'Kane Williomson': 60,
 'Kasun Rajitha': 61,
 'Keshav Maharaj': 62,
 'Kuldeep Yadav': 63,
 'Kusal Mendis': 64,
 'Kusal Perera': 65,
 'Kyle Jamieson': 66,
 'Lahiru Kumara': 67,
 'Liam_Stephen_Livingstone': 68,
 'Litton Das': 69,
 'Lockie Ferguson': 70,
 'Logan Verjus van Beek': 71,
 'Lungi Ngidi': 72,
 'M Saqib Zulfiqar': 73,
 'Maheesh Theekshana': 74,
 'Mahmudullah Riyad': 75,
 'Marco Jansen': 76,
 'Marcus Stoinis': 77,
 'Mark Chapman': 78,
 'Mark_Andrew_Wood': 79,
 'Marnus Labuschagne': 80,
 'Matheesha Pathirana': 81,
 'Matt Henry': 82,
 "Max O'Dowd": 83,
 'Mehidy Hasan': 84,
 'Mitchell Marsh': 85,
 'Mitchell Santner': 86,
 'Mitchell Starc': 87,
 'Moeen_Munir_Ali': 88,
 'Mohamad Nabi': 89,
 'Mohammad Babar Azam': 90,
 'Mohammad Nawaz': 91,
 'Mohammad Rizwan': 92,
 'Mohammad Wasim Jnr': 93,
 'Mohammed Shami': 94,
 'Mohammed Siraj': 95,
 'Mujeeb ur Rahman': 96,
 'Mushfiqur Rahim': 97,
 'Mustafizur': 98,
 'Najibullah Zadran': 99,
 'Najmul Hossain Shanto': 100,
 'Nasum Ahmed': 101,
 'Naveen ul Haq': 102,
 'Noor Ahmad': 103,
 'Pat Cummins': 104,
 'Pathum Nissanka': 105,
 'Paul Van Meekeren': 106,
 'Prasidh Krishna': 107,
 'Quinton de Kock': 108,
 'Rachin Ravindra': 109,
 'Rahmanullah Gurbaz': 110,
 'Rahmat Shah': 111,
 'Rashid Khan': 112,
 'Rassie van der Dussen': 113,
 'Ravindra Jadeja': 114,
 'Reece_James_William_Topley': 115,
 'Reeza Hendricks': 116,
 'Riaz Hasan': 117,
 'Roelof Erasmus Van der Merwe': 118,
 'Rohit Sharma': 119,
 'Ryan Klein': 120,
 'Sadeera Samarawickrama': 121,
 'Salman Ali Agha': 122,
 'Samuel_Matthew_Curran': 123,
 'Saud Shakeel': 124,
 'Scott Edwards': 125,
 'Sean Abbott': 126,
 'Shadab Khan': 127,
 'Shaheen Shah Afridi': 128,
 'Shakib Al Hasan': 129,
 'Shardul Thakur': 130,
 'Shariz Ahmad': 131,
 'Shoriful Islam': 132,
 'Shreyas Iyer': 133,
 'Shubman Gill': 134,
 'Steven Smith': 135,
 'Suryakumar Yadav': 136,
 'Sybrand Abraham_Engelbrecht': 137,
 'Tabraiz Shamsi': 138,
 'Tanzid Hasan': 139,
 'Tanzim Sakib': 140,
 'Taskin Ahmed': 141,
 'Temba Bavuma': 142,
 'Tim Southee': 143,
 'Tom Latham': 144,
 'Towhid Hridoy': 145,
 'Travis Head': 146,
 'Trent Boult': 147,
 'Usama Mir': 148,
 'Vikramjit Singh': 149,
 'Virat Kohli': 150,
 'Wesley Barresi': 151,
 'Will Young': 152}
 
  team = {'Afghanistan': 0,
 'Australia': 1,
 'Bangladesh': 2,
 'England': 3,
 'Netherlands': 4,
 'New Zealand': 5,
 'Pakistan': 6,
 'South Africa': 7,
 'SriLanka': 8,
 'india': 9}
  data[15] = ordinal_player.get(data[15],None)
  data[16] = team.get(data[16], None)
  data = standard_scaler.transform([data])
  return data

def conv(data,standard_scaler):
  ordinal_roll = {'Batsman': 0, 'Allrounder': 1, 'Bowler': 2,'Bowling Allrounder':3}
  ordinal_opposition = {'Australia': 0, 'South Africa': 1, 'Sri Lanka': 2,'England':3,'New Zealand':4,'Bangladesh':5,'Pakistan':6,'Afghanistan':7\
                   ,'India':8,'Netherlands':9}
  ordinal_player = {'Virat': 0, 'Rohit': 1, 'Ishan': 2,'Sheryas':3,'Rahul':4,'Shubman':5,'Hardik':6,'Jasprit':7,'Kuldeep':8,'Shami':9, \
                   'Axar':10,'Shardul':11,'Siraj':12,'Suryakumar':13,'Ashwin':14,'Jadeja':15,'Krishna':16,'Temba':17,'Quinton':18,\
                    'Rezza':19, 'Heinrich':20, 'Aiden':21, 'David':22, 'Rassie':23, 'Marco':24, 'Andile':25,'Gerald':26, 'Keshav':27\
                   , 'Lungi':28, 'Kagiso':29, 'Tabraiz':30, 'Lizzad':31,'Sisanda':32, 'Anrich':33}     
  ordinal_team = {'India':0,'South Africa':1}       
  data[8] = ordinal_team.get(data[8],None)
  data[7] = ordinal_roll.get(data[7], None)
  data[6] = ordinal_opposition.get(data[6], None)
  data[0] = ordinal_player.get(data[0], None)
  data = standard_scaler.transform([data])
  return data
def finali(data ,standard_scale):
    countries = {'India' : 1, 'South Africa' : 2 , 'Australia' : 3 , 'New Zealand' : 4 , 'Pakistan' : 5 , 
             'Afghanistan' : 6 , 'Sri Lanka' : 7 , 'Bangladesh' : 8 , 'Netherlands' : 9 , 'England' : 10 , 
             'Ireland' : 11 , 'UAE' : 12 , 'Qatar' : 13 , 'Zimbabwe' : 14 , 'West Indies' : 15}
    data[13]=countries.get(data[13],None)
    data[14]=countries.get(data[14],None)
    data[15]=countries.get(data[15],None)
    data=standard_scale.transform([data])
    return data


@app.get("/total_run", response_class=HTMLResponse)
async def total_run_form(request: Request):
    return templates.TemplateResponse("total_run.html", {"request": request})


@app.post("/predict-total-run", response_class=HTMLResponse)
async def predict_total_run(
    request: Request,
    Mat: float = Form(...),
    Inns: float = Form(...),
    Afghanistan: float = Form(...),
    Australia: float = Form(...),
    Bangladesh: float = Form(...),
    England: float = Form(...),
    India: float = Form(...),
    Netherlands: float = Form(...),
    NewZealand: float = Form(...),
    Pakistan: float = Form(...),
    SouthAfrica: float = Form(...),
    SriLanka: float = Form(...),
    AVG_Run: float = Form(...),
    AVG_SR: float = Form(...),
    AVG_BF: float = Form(...),
    Player_pre: str = Form(...),
    Team_pre: str = Form(...),
):
    data2 = co([Mat, Inns, Afghanistan, Australia, Bangladesh, England, India, Netherlands, NewZealand,
                Pakistan, SouthAfrica, SriLanka, AVG_Run, AVG_SR, AVG_BF, Player_pre, Team_pre], standard_2)
    prediction = total_run_model.predict(data2)

    return templates.TemplateResponse(
        "result_run.html", {"request": request, "prediction": prediction.tolist()}
        )
@app.get("/most_four", response_class=HTMLResponse)
async def most_four_form(request: Request):
    return templates.TemplateResponse("mostFours.html", {"request": request})

@app.post("/predict-most-four", response_class=HTMLResponse)
async def predict_most_four(
    request: Request,
    Mat: float = Form(...),
    Inns: float = Form(...),
    Afghanistan: float = Form(...),
    Australia: float = Form(...),
    Bangladesh: float = Form(...),
    England: float = Form(...),
    India: float = Form(...),
    Netherlands: float = Form(...),
    NewZealand: float = Form(...),
    Pakistan: float = Form(...),
    SouthAfrica: float = Form(...),
    SriLanka: float = Form(...),
    AVG_Run: float = Form(...),
    AVG_SR: float = Form(...),
    AVG_BF: float = Form(...),
    Player_pre: str = Form(...),
    Team_pre: str = Form(...),
):
    data2 = co([Mat, Inns, Afghanistan, Australia, Bangladesh, England, India, Netherlands, NewZealand,
                Pakistan, SouthAfrica, SriLanka, AVG_Run, AVG_SR, AVG_BF, Player_pre, Team_pre], standard_2)
    prediction = most_fours_model.predict(data2)

    return templates.TemplateResponse(
        "result.html", {"request": request, "prediction": prediction.tolist()}
        )
@app.get("/finalist_in", response_class=HTMLResponse)
async def finalis(request: Request):
    return templates.TemplateResponse("final.html", {"request": request})
#Prediction Function, return the predicted result in JSON
@app.post('/finalist', response_class=HTMLResponse)
async def predict(
    request: Request,
    team_matches: float = Form(...),
    team1_win: float = Form(...),
    team2_win: float = Form(...),
    team1_venue_matches: float = Form(...),
    team1_venue_win: float = Form(...),
    team2_venue_matches: float = Form(...),
    team2_venue_win: float = Form(...),
    team1_curr_match: float = Form(...),
    team1_curr_win: float = Form(...),
    team1_curr_perform: float = Form(...),
    team2_curr_match: float = Form(...),
    team2_curr_win: float = Form(...),
    team2_curr_perform: float = Form(...),
    team1_pre: str = Form(...),
    team2_pre: str = Form(...),
    venue_pre: str = Form(...),
    team1_win_to_lose: float = Form(...),
    team2_win_to_lose: float = Form(...),
):
    # Call the finali function with the appropriate parameters
    data2 = finali([team_matches, team1_win, team2_win, team1_venue_matches, team1_venue_win,
                    team2_venue_matches, team2_venue_win, team1_curr_match, team1_curr_win,
                    team1_curr_perform, team2_curr_match, team2_curr_win, team2_curr_perform,
                    team1_pre, team2_pre, venue_pre, team1_win_to_lose, team2_win_to_lose], standard_1)

    # Assuming `finalists_model` is defined somewhere in your code
    prediction = finalists_model.predict(data2)

    if prediction[0] < 0.50:
        predictio = team2_pre
    else:
        predictio = team1_pre

    return templates.TemplateResponse(
        "result_finalist.html", {"request": request, "prediction": predictio}
    )
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/player", response_class=HTMLResponse)
async def player_form(request: Request):
    return templates.TemplateResponse("player.html", {"request": request})

@app.post("/predict-player", response_class=HTMLResponse)
async def predict_player(
    request: Request,
    Name: str = Form(...),
    bat_score: float = Form(...),
    bow_score: float = Form(...),
    all_bat: float = Form(...),
    all_bow: float = Form(...),
    wkt: float = Form(...),
    Oppsition: str = Form(...),
    Roll: str = Form(...),
    Team: str = Form(...),
):
    data2 = conv([Name, bat_score, bow_score, all_bat, all_bow, wkt, Oppsition, Roll, Team], standard)
    prediction = model.predict(data2)

    return templates.TemplateResponse(
        "prediction.html", {"request": request, "prediction": prediction.tolist()}
    )

#Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    

#Command to run API server   
#python -m uvicorn main:app --reload

