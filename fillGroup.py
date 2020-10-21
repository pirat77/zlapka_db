import dao
import random


def genRandomName(adjectives, nouns):
    adjective = adjectives[random.randrange(len(adjectives))]
    noun = nouns[random.randrange(len(nouns))]
    return f"""{adjective} {noun}"""

def main():
    adjectivesFile = open("./media/adjectives.txt", "r")
    nounsFile = open("./media/noun.txt")

    adjectives = []
    nouns = []

    for line in adjectivesFile:
        adjectives.append(line.replace("\n", "").replace("\r", ""))

    for line in nounsFile:
        nouns.append(line.replace("\n", "").replace("\r", ""))

    
    for _ in range(1000):
        dao.insert_group(genRandomName(adjectives, nouns), bool(random.getrandbits(1)))

main()