from access_log.models import UsageLog


def add_log(building, user):
    """Create a log entry for the given building and user."""
    new_log = UsageLog(building=building, user=user)
    new_log.save()
