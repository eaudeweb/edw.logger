import abc
import logging
import traceback
import json
from edw.logger.events import ZOPE_STATUS

logger = logging.getLogger("edw.logger")


class BaseEvent(object):
    __metaclass__ = abc.ABCMeta

    _fail_msg = ''
    _event = None

    def __call__(self, context, event):
        if not ZOPE_STATUS['ready']:
            return

        if self._skip(context, event):
            return

        try:
            result = self.log(context, event)
            if result:
                logger.info(json.dumps(result))
        except:
            tb = traceback.format_exc()
            logger.error(json.dumps(self.fail(tb)))

    @abc.abstractmethod
    def log(self, context, event):
        pass

    def fail(self, tb):
        return {
            "Type": "LogError",
            "Message": self._fail_msg,
            "Traceback": tb,
        }

    def _skip(self, context, event):
        """ Skip logging.
        """
        return False
