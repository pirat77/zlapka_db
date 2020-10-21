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
def insert_organization(cursor, org_name):
    cursor.execute("""INSERT INTO organization (name) VALUES (%s);""", (org_name))
    
@connection.connection_handler
def fill_preferences_table(cursor):
    id = 1
    sql = "INSERT INTO zlapka.preference VALUES "
    preferencesFile = open("./media/preferencesList.txt", "r")
    for line in preferencesFile:
        value = line.replace("\n", "").replace("\r", "")
        if id != 1:
            sql += ","
        sql += f"""({id},'{value}')"""
        id += 1
    sql += ";"
    cursor.execute(sql)

@connection.connection_handler
def insert_event_category(cursor, event_category_name):
    cursor.execute("""INSERT INTO zlapka.event_category (name) VALUES ('{event_category_name}');""")


