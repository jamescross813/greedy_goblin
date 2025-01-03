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


def find_best_night(availability_table):
   best_night= '' 
   big_num = 0
   for x in availability_table:
      if availability_table[x] > big_num:
         big_num = availability_table[x]
         best_night = x
   return best_night

find_best_night(count_availability)


def available_on_night(gamers, game_night):
   attending_game_night = []
   for a in gamers:
      for b in a['availability']:
         if b == game_night:
            attending_game_night.append(a['name'])
   # print(attending_game_night)
   return attending_game_night

# available_on_night(gamers, find_best_night(count_availability))

form_email = 'Hello {}! This week on {} we will be hosting {}. So come and join us!'

def send_email(gamers_who_can_attend, day, game):
   for x in gamers_who_can_attend:
      # print(x)
      print(form_email.format(x, day, game))

send_email(available_on_night(gamers, find_best_night(count_availability)), find_best_night(count_availability), "Abruptly Goblins!")
