import connection

@connection.connection_handler
def fill_preferences_table(cursor):
    id = 1
    sql = "INSERT INTO preference VALUES "
    preferencesFile = open("zlapka_db/preferencesList.txt", "r")
    for line in preferencesFile:
        value = line.replace("\n", "").replace("\r", "")
        if id != 1:
            sql += ","
        sql += f"""({id},'{value}')"""
        id += 1
    sql += ";"
    cursor.execute(sql)
    
    

fill_preferences_table()