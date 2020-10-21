import connection
import dao
    

preferencesFile = open("./media/preferencesList.txt", "r")
for line in preferencesFile:
    value = line.replace("\n", "").replace("\r", "")
    dao.insert_preference(value)
