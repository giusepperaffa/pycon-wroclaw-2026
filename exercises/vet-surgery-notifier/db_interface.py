class FailedDatabaseConnection(Exception):
    pass


def get_active_subscriptions(date):
    try:
        ...
    except:
        raise FailedDatabaseConnection("Failed database connection!")

