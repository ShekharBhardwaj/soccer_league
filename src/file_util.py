import csv
import json
import logging
import sys

def csv_to_json (csv_file_name_str, json_file_name_str):
    try:
        logging.info("converting {} to {}".format(csv_file_name_str, json_file_name_str))
        csv_file = open(csv_file_name_str, "r")
        json_file = open(json_file_name_str, "w")
        
        field_names = ["Name", "Height", "SoccerExperience", "GuardianName" ]
        reader = csv.DictReader(csv_file, field_names)
        logging.info("Conversion finish.")
        out = '{\n "Players": [\n\t'+ ',\n\t'.join([json.dumps(row) for row in reader]) + '\n]\n}'
        json_file.write(out)
        return json_file_name_str
    except (OSError, IOError, TypeError) as e:
        logging.error("csv to json conversion failed: Caused by -> {}".format(e))
        

def load_json(json_file_name_str):
    
    try:
        with open(json_file_name_str) as json_file:
            data = json.load(json_file)
            return data
    except (TypeError) as e:
        logging.error("Json file loading failed: Caused by -> {}".format(e))




if __name__ == "__main__":
    try:
        logging.debug("Running module from main")
        csv_to_json (sys.argv[1], sys.argv[2])
        data = load_json(sys.argv[2])
        print(data["Players"][1]["Name"])
    except (TypeError) as e:
        logging.error("Json file loading failed: Caused by -> {}".format(e))
    
    
    
    