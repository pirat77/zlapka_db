import dao
from decouple import config


# user_name = config('PSQL_USER_NAME')
# password = config('PSQL_PASSWORD')
# host = config('PSQL_HOST')
# database_name = config('PSQL_DB_NAME')

# env_variables_defined = user_name and password and host and database_name
# if env_variables_defined:
#     # this string describes all info for psycopg2 to connect to the database
#     print('postgresql://{user_name}:{password}@{host}/{database_name}'.format(
#         user_name=user_name,
#         password=password,
#         host=host,
#         database_name=database_name
#         )
#     )

print(dao.get_organization())