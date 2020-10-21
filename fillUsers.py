import connection
import random

preferencesIdInDB = 0
locationsIdInDB = 0
userCategoriesIdInDB = 0

@connection.connection_handler
def fill_user_table(cursor):
    firstNamesFile = open("./media/first_names.txt", "r")
    lastNamesFile = open("./media/last_names.txt", "r")
    lastNamesList = []
    for lastName in lastNamesFile:
        value = lastName.replace("\n", "").replace("\r", "")
        lastNamesList.append(value)
    index = 1
    for line in firstNamesFile:
        firstValue = True
        firstName = line.replace("\n", "").replace("\r", "")

        for lastName in lastNamesList:
            sql = generate_insert_command(index, firstName, lastName)
            cursor.execute(sql)
            index += 1


def generate_email(firstName, lastName, index):
    subFirst = firstName[0:1]
    subLast = lastName[0:1]
    return f"""{subFirst}.{subLast}.{index}@gmail.com"""

def generate_insert_command(index, firstName, lastName):
    location_id = random.randint(1, locationsIdInDB)
    category_id = 1
    if (index <= 51):
        category_id = 2
    elif (index <= 200):
        category_id = 3
    elif (index <= 5000):
        category_id = 4
    preferencesList = pick_preferences_id_list()
    preferences = ", ".join(preferencesList)
    email = generate_email(firstName, lastName, index)

    return f"""INSERT INTO zlapka.users VALUES ({index},'{firstName}','{lastName}',
            CONCAT('Hi! My name is {firstName} and I live in ',
            (SELECT name FROM zlapka.location WHERE location_id = {location_id}),
            '. Things I''m interested in: ',
            (SELECT string_agg(name, ', ') FROM zlapka.preference WHERE preference_id IN ({preferences}))),
            'path/to/photo', '{email}', {location_id}, {category_id});
            {generate_user_preferences_insert_command(preferencesList, index)}"""

def generate_user_preferences_insert_command(preferencesList, userIndex):
    sql = "INSERT INTO zlapka.user_preference (user_id, preference_id) VALUES "
    firstRecord = True
    for preferenceId in preferencesList:
        if (firstRecord == False):
            sql += ","
        sql += f"""({userIndex}, {preferenceId})"""
        firstRecord = False
    sql += ";"
    return sql

@connection.connection_handler
def count_elements_in_table(cursor, tableName):
    cursor.execute(f"""SELECT COUNT(*) FROM {tableName};""")
    result = cursor.fetchone()["count"]
    return result

def pick_preferences_id_list():
    preferencesList = []
    numberOfPreferences = random.randint(1, 5)
    while (len(preferencesList) < numberOfPreferences):
        random_id = random.randint(1, preferencesIdInDB)
        if random_id in preferencesList:
            break
        preferencesList.append(str(random_id))
    return preferencesList

def assign_variables():
    global preferencesIdInDB 
    global locationsIdInDB 
    global userCategoriesIdInDB 
    preferencesIdInDB = count_elements_in_table("zlapka.preference")
    locationsIdInDB = count_elements_in_table("zlapka.location")
    userCategoriesIdInDB= count_elements_in_table("zlapka.user_category")

assign_variables()
fill_user_table()