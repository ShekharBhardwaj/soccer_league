import file_util
import random


def dividing_players(csv_file_name_str):

    team1 = []
    team2 = []
    team3 = []

    exp_playa= []
    non_exp_playa=[]
    json_output = file_util.csv_to_json(csv_file_name_str)
    list_of_players = json_output["Players"]
    del list_of_players[0]

    for player in list_of_players:
        if player["SoccerExperience"] == "YES" and player["Name"] != "Name":
            exp_playa.append(player)
        else:
            non_exp_playa.append(player)

    random.shuffle(exp_playa)
    random.shuffle(non_exp_playa)

    team1.extend(exp_playa[0:3])
    team2.extend(exp_playa[3:6])
    team3.extend(exp_playa[6:])

    team1.extend(non_exp_playa[0:3])
    team2.extend(non_exp_playa[3:6])
    team3.extend(non_exp_playa[6:])

    return [team1, team2, team3]


def template(gaurdians,playername, team, jerseynumber):
    greetings = "Dear {}\n \n".format(gaurdians)
    subject = "Subject: Soccer Tournament practice session commencement\n \n"
    message1 = "   Your ward {}, is playing for Team {}, {} is going to dawn the Jersey Number {}.\n".format(playername, team, playername, jerseynumber)
    message2 ="We would like you to bring {} for their first day of practice session on Jul 27 2017, 4 PM to 7PM. \n \n".format(playername)
    closing = "Regards \n Game Co-ordinator\n Jun 27 2017"

    return greetings+subject+message1+message2+closing

def file_io(all_teams):

    teams = ["Dragons", "Sharks", "Raptors"]
    with open("__teams.txt__", "w") as team_file:
        for team_x in all_teams:
            rand_team_name = random.choice(teams)
            team_file.write("Team Name: {} \n".format(rand_team_name))
            team_file.write(" {} | {} | {} |  {} \n".format(file_util.NAME_HEADER, file_util.HIGHT_HEADER,
                                                            file_util.SOCCER_EXP_HEADER, file_util.GAURDIAN_NAME_HEADER))
            teams.remove(rand_team_name)
            for player in team_x:
                team_file.write(" {} | {} | {} |  {} \n".format(player["Name"], player["Height"], player["SoccerExperience"], player["GuardianName"]))
                player_file_name = player["Name"].replace(" ", "_").lower()
                with open(player_file_name+".txt", "w") as player_file:
                    player_file.write(template(player["GuardianName"], player["Name"], rand_team_name, player["JerseyNumber"]))

def gen_digest(csv_file):
    file_io(dividing_players(csv_file))

if __name__ == "__main__":
    list_teams = dividing_players("soccer_players.csv")
    file_io(list_teams)









