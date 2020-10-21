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
    cursor.execute(f"""INSERT INTO zlapka.organization (name) VALUES ('{org_name}');""")
    
@connection.connection_handler
def insert_preference(cursor, preference_name):
    cursor.execute(f"""INSERT INTO zlapka.preference (name) VALUES ('{preference_name}');""")

@connection.connection_handler
def insert_event_category(cursor, event_category_name):
    cursor.execute(f"""INSERT INTO zlapka.event_category (name) VALUES ('{event_category_name}');""")


