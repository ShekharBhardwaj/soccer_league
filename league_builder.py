import players_util


# Function to be called when this module is imported, pass csv name
#  file as an argument.
def generate_teams(csv_file):
    players_util.gen_digest(csv_file)


if __name__ == "__main__":
    generate_teams("soccer_players.csv")


