import dao
import random

def main():
    citiesFile = open("./media/cityTags.txt", "r")
    
    for line in citiesFile:
        lineArray = (line.replace("\n", "").replace("\r", "").replace("\t", "").split(","))
        geoTag = "'{" + str(lineArray[1]) + ", " + str(lineArray[2]) + ",0}'" 
        dao.insert_city(lineArray[0], geoTag)

main()