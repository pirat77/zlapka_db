import connection
from dao import count_elements_in_table

amountOfRowsPerTransaction = 1000000

@connection.connection_handler
def fill_user_relations(cursor):
    numberOfRows = 0
    statusList = ['USER1_BLOCKED_USER2','USER2_BLOCKED_USER1','USER1_INVITED_USER2',
            'USER2_INVITED_USER1','USER1_ACCEPTED_USER2','USER2_ACCEPTED_USER1']
    usersInDB = count_elements_in_table("zlapka.users")
    friendsToAddPerUser = 10
    firstLineSql = "INSERT INTO zlapka.user_relations (status, user_id_1, user_id_2) VALUES "
    sql = firstLineSql
    firstValue = True
    for idUser in range(1, usersInDB - friendsToAddPerUser + 1):
        firstFriend = idUser + 1
        for idFriend in range(firstFriend, firstFriend + friendsToAddPerUser):
            if (firstValue == False):
                sql += ","
            else:
                firstValue = False
            sql += f"""('{statusList[idUser % len(statusList)]}',
            {idUser},{idFriend})"""
            numberOfRows += 1
        if (numberOfRows >= amountOfRowsPerTransaction):
            print(amountOfRowsPerTransaction, "reached")
            cursor.execute(sql)
            numberOfRows = 0
            firstValue = True
            sql = firstLineSql
    if (len(sql) != len(firstLineSql)):
        cursor.execute(sql)


fill_user_relations()

