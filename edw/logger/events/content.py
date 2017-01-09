from datetime import datetime

import zope.lifecycleevent.interfaces as zci
from zope.container.interfaces import IContainerModifiedEvent

from Products.Five.utilities.interfaces import IMarkerInterfaces

from edw.logger.util import get_user_data
from edw.logger.events.base import BaseEvent


class ObjectEvent(BaseEvent):
    """ Base class for content events.
    """

    _action = None
    _fail_msg = "Could not log object action."

    def log(self, obj, event):
        user_data = get_user_data(obj.REQUEST or None)

        return {
            "IP": user_data['ip'],
            "User": user_data['user'],
            "Date": datetime.now().isoformat(),
            "URL": obj.absolute_url(),
            "Type": self._action,
        }

    def fail(self, tb):
        result = super(ObjectEvent, self).fail(tb)
        result["EventType"] = self._action
        return result


class ObjectCreatedEvent(ObjectEvent):
    _action = "Create"

    def _skip(self, obj, event):
        return zci.IObjectCopiedEvent.providedBy(event)


class ObjectMovedEvent(ObjectEvent):
    _action = "Move"

    def log(self, obj, event):
        if event.oldParent:
            return self.log_move(obj, event)

        return self.log_copy(obj, event)

    def log_move(self, obj, event):
        result = super(ObjectMovedEvent, self).log(obj, event)
        result['OldPath'] = '{}/{}'.format(
            event.oldParent.absolute_url(), event.oldName)
        return result

    def log_copy(self, obj, event):
        result = super(ObjectMovedEvent, self).log(obj, event)
        result['Type'] = 'Paste'

    def _skip(self, obj, event):
        return zci.IObjectRemovedEvent.providedBy(event)


class ObjectCopiedEvent(ObjectEvent):
    _action = "Copy"

    def log(self, obj, event):
        result = super(ObjectCopiedEvent, self).log(event.original, event)
        result['Original'] = event.original.absolute_url()
        result['CopyName'] = obj.getId()
        return result


class ObjectModifiedEvent(ObjectEvent):
    _action = "Modify"

    def _skip(self, obj, event):
        return IContainerModifiedEvent.providedBy(event)


class ObjectAddedEvent(ObjectEvent):
    _action = "Add"

    def _skip(self, obj, event):
        return zci.IObjectMovedEvent.providedBy(event)


class ObjectRemovedEvent(ObjectEvent):
    _action = "Remove"


handler_removed = ObjectRemovedEvent()
handler_added = ObjectAddedEvent()
handler_modified = ObjectModifiedEvent()
handler_created = ObjectCreatedEvent()
handler_moved = ObjectMovedEvent()
handler_copied = ObjectCopiedEvent()
