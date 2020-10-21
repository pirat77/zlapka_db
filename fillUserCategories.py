import dao

for user_category in {"end user", "moderator", "administrator", "publisher"}:
    dao.insert_user_category(user_category)