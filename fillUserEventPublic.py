import dao
import random

def main():
    user_list = dao.list_user_id()
    city_list = dao.list_city_id()
    
    for user in range(len(user_list)):
        event_list = dao.list_available_event(city_list[random.randrange(len(city_list))])
        if (len(event_list)>0):
            for event in range(random.randrange(0, len(event_list))):
                dao.insert_user_event(event_list[event], user_list[user])

main()