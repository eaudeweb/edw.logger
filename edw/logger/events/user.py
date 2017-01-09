from datetime import datetime

from edw.logger.util import get_ip
from edw.logger.events.base import BaseEvent


class UserLoginEvent(BaseEvent):

    _fail_msg = "Could not log user login."

    def log(self, user, event):
        return {
            "IP": get_ip(user.REQUEST),
            "User": user.getUserName(),
            "Date": datetime.now().isoformat(),
            "Type": "Login",
        }

handler_login = UserLoginEvent()