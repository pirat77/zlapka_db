import connection
import dao
    
@connection.connection_handler
def fill_preferences_table(cursor):
    preferencesFile = open("./media/preferencesList.txt", "r")
    for line in preferencesFile:
        value = line.replace("\n", "").replace("\r", "")
        dao.insert_preference(value)
