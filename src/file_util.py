import csv
import json
import logging
import sys
import random


# 
# def csv_to_json (csv_file_name_str):
#     try:
#         logging.info("converting {} ".format(csv_file_name_str))
#         csv_file = open(csv_file_name_str, "r")
#         #json_file = open(json_file_name_str, "w")
#         
#         field_names = ["Name", "Height", "SoccerExperience", "GuardianName", "JerseyNumber"]
#         reader = csv.DictReader(csv_file, field_names)
#         logging.info("Conversion finish.")
#         out = '{\n "Players": [\n\t'+ ',\n\t'.join([json.dumps(row) for row in reader]) + '\n]\n}'
#         #json_file.write(out)
#         return out
#     except (OSError, IOError, TypeError) as e:
#         logging.error("csv to json conversion failed: Caused by -> {}".format(e))
#         
PLAYERS_JSON_FILE_NAME = "soccre_players.json"

def generate_jersey_number():
    return "".join(str(random.sample(range(1, 99), 2)))

def csv_to_json(csv_file_name_str):
    field_names = ["Name", "Height", "SoccerExperience",
                   "GuardianName", "JerseyNumber"]
    # Read the rows of your CSV as dictionaries
    with open(csv_file_name_str, "r") as csv_file:
        reader = csv.DictReader(csv_file, field_names)
        data = {
            'Players': [player for player in reader]
        }
    # Loop over your players, assigning them a jersey number
    for player in data['Players']:
        player['JerseyNumber'] = generate_jersey_number()
    # Dump the entire data structure to JSON
    with open(PLAYERS_JSON_FILE_NAME, "w") as json_file:
        json.dump(data, json_file)
    return data
        

if __name__ == "__main__":
    try:
        logging.debug("Running module from main")
        print(csv_to_json (sys.argv[1])["Players"][2]["Name"])
        
    except (TypeError) as e:
        logging.error("Json file loading failed: Caused by -> {}".format(e))
    
    
    
    