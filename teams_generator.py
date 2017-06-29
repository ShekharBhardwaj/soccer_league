import players_util
import sys


def generate_teams(csv_file):
    players_util.gen_digest(csv_file)


if __name__ == "__main__":
    generate_teams(sys.argv[1])