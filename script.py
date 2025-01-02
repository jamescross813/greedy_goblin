gamers = []

def add_gamer(gamer, gamers_list):
    if gamer['name'] != "" and gamer['availability'] != "":
        gamers_list.append(gamer)

kimberly = {'name':'Kimberly Warner','availability': ["Monday", "Tuesday", "Friday"]}

add_gamer(kimberly, gamers)

def build_daily_frequency_table():
    days_of_week = {'Monday': 0, 'Tuesday': 0, 'Wednesday': 0, 'Thursday': 0, 'Friday': 0, 'Saturday': 0, 'Sunday': 0}
    return days_of_week

count_availability = build_daily_frequency_table()

add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

def caluclate_availability(gamers_list, availability_frequency):
    for i in gamers_list:
       for j in i['availability']:
         for k in count_availability:
            if k == j:
               count_availability[k] +=1
         return count_availability

caluclate_availability(gamers, count_availability)

