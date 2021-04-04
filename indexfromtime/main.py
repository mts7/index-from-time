from datetime import datetime
from time import time
import sys


def get_index(length: int):
    """Gets an integer between 0 and the length provided based on the time and day of the year.

    Parameters
    ----------
    length : int

    Returns
    -------
    int
    """
    # get the current Unix timestamp as an integer
    seconds = int(time())
    # get the current day of the year
    day = datetime.now().timetuple().tm_yday

    # add the seconds to the day of the year
    total = seconds + day

    # get a value that is between 0 and the length - 1 based on the current time
    return total % (length - 1)


if __name__ == '__main__':
    print(get_index(int(sys.argv[1])))
