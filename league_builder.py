import players_util
import sys


# Function to be called when this module is imported, pass csv name
#  file as an argument.
def generate_teams(csv_file):
    players_util.gen_digest(csv_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need to pass csv file name")
    else:
        generate_teams(sys.argv[1])


