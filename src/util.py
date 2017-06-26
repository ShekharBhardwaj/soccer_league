import csv
import json
import logging
import sys

def file_loca_nam (csv_file_name_str, json_file_name_str):
    try:
        logging.info("converting {} to {}".format(csv_file_name_str, json_file_name_str))
        csv_file = open(csv_file_name_str, "r")
        json_file = open(json_file_name_str, "w")
        
        field_names = ["Name", "Height", "SoccerExperience", "GuardianName" ]
        reader = csv.DictReader(csv_file, field_names)
        logging.info("Conversion finish.")
        out = "[\n\t" + ",\n\t".join([json.dumps(row) for row in reader]) + "\n]"
        json_file.write(out)
    except (OSError, IOError, TypeError) as e:
        logging.error("csv to json conversion failed: Caused by -> {}".format(e))
        






if __name__ == "__main__":
    logging.debug("Running module from main")
    file_loca_nam (sys.argv[1], sys.argv[2])
    
    
    
    
    