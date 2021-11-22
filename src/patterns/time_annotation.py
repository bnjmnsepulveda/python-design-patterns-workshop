import time

def time_minutes(method):
    """
    Decorator which first truncates our table and then measures the time it takes for a method call.
    In this case, the method call is inserting data into a table.
    """

    def timed(*args, **kwargs):
        # truncate the table before every method call
        ts = time.time()
        data = method(*args, **kwargs)
        # connection.commit()
        te = time.time()
        secs = round(te - ts)
        minutes = round(secs / 60)
        seconds = secs % 60
        if secs < 60:
            seconds = secs
            minutes = 0

        print(
            "{method} took {minutes} minutes {secs} seconds".format(
                method=method.__name__, minutes=minutes, secs=seconds
            )
        )
        return data

    return timed