import gi

gi.require_version("IgnisNotificationsGLib", "0.1")

from gi.repository import IgnisNotificationsGLib

global NOTIFICATIONS_SERVICE
NOTIFICATIONS_SERVICE = None


def get_notification_service() -> IgnisNotificationsGLib.Service:
    global NOTIFICATIONS_SERVICE

    if NOTIFICATIONS_SERVICE:
        return NOTIFICATIONS_SERVICE
    else:
        service = IgnisNotificationsGLib.Service.new()
        service.run_async(None, lambda x, res: service.run_finish(res))
        NOTIFICATIONS_SERVICE = service
        return service
