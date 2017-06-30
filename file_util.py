import csv
import json
import random

PLAYERS_JSON_FILE_NAME = "soccre_players.json"
NAME_HEADER = "Name"
HIGHT_HEADER = "Height (inches)"
SOCCER_EXP_HEADER = "Soccer Experience"
GAURDIAN_NAME_HEADER = "Guardian Name(s)"
JEARSY_NUMBER_HEADER = "Jersey Number"
TEAM_NAME = HEADER = "Team Name"


def csv_to_json(csv_file_name_str):
    jersy_numbers = ["22", "77", "99", "13", "15", "7", "09", "44", "66", "98", "100", "65", "12", "63", "47", "70", "61", "55", "11"]
    field_names = ["Name", "Height", "SoccerExperience",
                   "GuardianName", "JerseyNumber"]
    # Read the rows of your CSV as dictionaries
    with open(csv_file_name_str, "r") as csv_file:
        reader = csv.DictReader(csv_file, field_names)
        data = {
            'Players': [player for player in reader]
        }
    # Adding the Jersey Numbers to the json file
    for player in data['Players']:
        jnum = random.choice(jersy_numbers)
        player['JerseyNumber'] = jnum
        jersy_numbers.remove(jnum)
    # Saving the json file
    with open(PLAYERS_JSON_FILE_NAME, "w") as json_file:
        json.dump(data, json_file)
    return data
        


    
    
    
    