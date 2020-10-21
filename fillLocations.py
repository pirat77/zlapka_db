import dao
import random

def genRandomName(adjectives, nouns):
    adjective = adjectives[random.randrange(len(adjectives))]
    noun = nouns[random.randrange(len(nouns))]
    return f"""{adjective} {noun}"""

def main():
    adjectivesFile = open("./media/adjectivesForLocations.txt", "r")
    nounsFile = open("./media/nounsForLocations.txt")

    adjectives = []
    nouns = []

    for line in adjectivesFile:
        adjectives.append(line.replace("\n", "").replace("\r", ""))

    for line in nounsFile:
        nouns.append(line.replace("\n", "").replace("\r", ""))

    for _ in range(1000):
        geoTag = "'{" + str(random.randrange(-180, 180)) + ", " + str(random.randrange(-180, 180)) + ", " + str(random.randrange(300)) + "}'" 
        dao.insert_location(genRandomName(adjectives, nouns), geoTag)

main()