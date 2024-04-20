import datetime

def get_date_time_n_secs_ago(sec: int):
    """
    This function calculates the time n seconds ago.

    Args:
        sec (int): Number of seconds ago time needed.

    Returns:
        str: ISO formatted datetime string.
    """
    utc_time = datetime.datetime.utcnow() - datetime.timedelta(seconds=sec)
    return utc_time.isoformat()
