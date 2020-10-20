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
    




