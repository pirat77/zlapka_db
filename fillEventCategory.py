import dao

eventCategoryListFile = open("./media/eventCategoryList.txt", "r")
for line in eventCategoryListFile:
    value = line.replace("\n", "").replace("\r", "")
    dao.insert_event_category(value)        