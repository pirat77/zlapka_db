import connection
from dao import count_elements_in_table

groupsInDB = 0
usersInDB = 0

@connection.connection_handler
def fill_user_group(cursor):
    idUser = 1
    sql = "INSERT INTO zlapka.user_group VALUES "
    firstValue = True
    while (idUser <= usersInDB):
        if (firstValue == False):
            sql += ","
        else:
            firstValue = False
        sql += f"""({idUser}, {idUser%1000 + 1}, {idUser})"""
        idUser += 1
    cursor.execute(sql)

def assign_variables():
    global groupsInDB
    global usersInDB
    groupsInDB = count_elements_in_table("zlapka.group")
    usersInDB = count_elements_in_table("zlapka.users")

assign_variables()
fill_user_group()