from dao import insert_voucher
from dao import count_elements_in_table
from random import randint

usersInDB = count_elements_in_table("zlapka.users")
idUser = 1

while (idUser < usersInDB):
    discount = randint(1, 300)
    insert_voucher("DISCOUNT", discount, idUser)
    idUser += 20