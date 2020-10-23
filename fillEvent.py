import dao
import random
import time

def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    https://stackoverflow.com/questions/553303/generate-a-random-date-between-two-other-dates
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y %I:%M %p', prop)

def genRandomName(adjectives, verbs):
    adjective = adjectives[random.randrange(len(adjectives))]
    verb = verbs[random.randrange(len(verbs))]
    return f"""{adjective} {verb}"""

def main():
    adjectivesFile = open("./media/adjectives.txt", "r")
    verbsFile = open("./media/verbs.txt")

    adjectives = []
    verbs = []

    for line in adjectivesFile:
        adjectives.append(line.replace("\n", "").replace("\r", ""))

    for line in verbsFile:
        verbs.append(line.replace("\n", "").replace("\r", ""))

    category_list = dao.list_event_category_id()
    location_list = dao.list_event_location_id()
    org_list = dao.list_organization_id()

    for _ in range(20000):
        name = genRandomName(adjectives, verbs)
        description = f"""{genRandomName(adjectives, verbs)}! {genRandomName(adjectives, verbs)}, {genRandomName(adjectives, verbs)}, {genRandomName(adjectives, verbs)}! Take your friends!"""
        max_participant = random.randrange(10, 1000)
        date = random_date("10/10/2020 1:30 PM", "12/12/2025 4:50 AM", random.random())
        duration = random.randrange(30, 480)
        public =  random.randrange(10, 10000) < max_participant
        category_id = category_list[random.randrange(len(category_list))]
        location_id = location_list[random.randrange(len(location_list))]
        organization_id = org_list[random.randrange(len(org_list))]
        dao.insert_event(name, description, max_participant, date, duration, public, category_id, location_id, organization_id)

main()