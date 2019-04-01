import datetime
import random
import string


def generateRandomString(size):
    return ''.join([random.choice(string.ascii_letters) for n in range(size)])


def generateRandomDate():
    start = datetime.datetime(1980, 1, 1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None)
    end = datetime.datetime.now()
    return start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds()))
    )
