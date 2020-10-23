import connection
import util
from operator import itemgetter

@connection.connection_handler
def get_organization(cursor, organization_id=None):
    if organization_id:
        cursor.execute("""SELECT * FROM zlapka.organization WHERE organization_id = (%s)""", (organization_id,))
        answers = [dict(row) for row in cursor.fetchall()]
    else:
        cursor.execute("""SELECT * FROM zlapka.organization""")
        answers = [dict(row) for row in cursor.fetchall()]
    return answers

@connection.connection_handler
def insert_event(cursor, name, description, max_participant, date, duration, public, event_category, event_location, event_organization):
    cursor.execute(f"""INSERT INTO zlapka.event (name, description, max_participant, date, duration, public, 
                                                    event_category_id, event_location_id, event_organization_id) 
                        VALUES ('{name}', '{description}', '{max_participant}', '{date}', '{duration}', '{public}', '{event_category}',
                                '{event_location}', '{event_organization}');""")

@connection.connection_handler
def list_available_event(cursor, city):
    cursor.execute(f"""select * from analitics.local_events({city});""")
    events = []
    for row in cursor.fetchall():
        events.append(row['event_id'])
    return events        

@connection.connection_handler
def list_event_id(cursor):
    cursor.execute("""SELECT event_id FROM zlapka.event""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['event_id'])
    return answers

@connection.connection_handler
def list_public_event_id(cursor):
    cursor.execute("""SELECT event_id FROM zlapka.event as e WHERE e.public='true'""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['event_id'])
    return answers

@connection.connection_handler
def list_user_id(cursor):
    cursor.execute("""SELECT user_id FROM zlapka.users""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['user_id'])
    return answers

@connection.connection_handler
def list_event_category_id(cursor):
    cursor.execute("""SELECT category_id FROM zlapka.event_category""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['category_id'])
    return answers

@connection.connection_handler
def list_event_location_id(cursor):
    cursor.execute("""SELECT location_id FROM zlapka.location;""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['location_id'])
    return answers

@connection.connection_handler
def list_organization_id(cursor):
    cursor.execute("""SELECT organization_id FROM zlapka.organization;""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['organization_id'])
    return answers

@connection.connection_handler
def list_city_id(cursor):
    cursor.execute("""SELECT city_id FROM zlapka.city;""")
    answers = [] 
    for row in cursor.fetchall():
        answers.append(row['city_id'])
    return answers

@connection.connection_handler
def insert_user_event(cursor, event_id, user_id):
    cursor.execute(f"""INSERT INTO zlapka.user_event (event_id, user_id) VALUES ('{event_id}', '{user_id}');""")

@connection.connection_handler
def insert_city(cursor, city_name, geo_tag):
    cursor.execute(f"""INSERT INTO zlapka.city (name, geotag) VALUES ('{city_name}', {geo_tag});""")

@connection.connection_handler
def insert_location(cursor, location_name, geo_tag):
    cursor.execute(f"""INSERT INTO zlapka.location (name, geo_tag) VALUES ('{location_name}', {geo_tag});""")

@connection.connection_handler
def insert_user_category(cursor, user_category_name):
    cursor.execute(f"""INSERT INTO zlapka.user_category (name) VALUES ('{user_category_name}');""")

@connection.connection_handler
def insert_group(cursor, group_name, public):
    cursor.execute(f"""INSERT INTO zlapka.group (name, public) VALUES ('{group_name}', '{public}');""")

@connection.connection_handler
def insert_organization(cursor, org_name):
    cursor.execute(f"""INSERT INTO zlapka.organization (name) VALUES ('{org_name}');""")
    
@connection.connection_handler
def insert_preference(cursor, preference_name):
    cursor.execute(f"""INSERT INTO zlapka.preference (name) VALUES ('{preference_name}');""")

@connection.connection_handler
def insert_event_category(cursor, event_category_name):
    cursor.execute(f"""INSERT INTO zlapka.event_category (name) VALUES ('{event_category_name}');""")

@connection.connection_handler
def insert_voucher(cursor, voucher_type, value, user_id):
    cursor.execute(f"""INSERT INTO zlapka.voucher (type, value, user_id) VALUES ('{voucher_type}', {value}, {user_id});""")

@connection.connection_handler
def count_elements_in_table(cursor, tableName):
    cursor.execute(f"""SELECT COUNT(*) FROM {tableName};""")
    result = cursor.fetchone()["count"]
    return result
