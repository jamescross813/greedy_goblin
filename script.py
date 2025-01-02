gamers = []

def add_gamer(gamer, gamers_list):
    if gamer['name'] != "" and gamer['availability'] != "":
        gamers_list.append(gamer)

kimberly = {'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)


