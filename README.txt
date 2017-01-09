Installation
============

::

    [instance]
    ...
    eggs =
        ...
        edw.logger
    zcml =
        ...
        edw.logger


Introduction
============

This package creates a new logfile in var/log. Logging is done in JSON format.

The folowing events are logged:

    * Login (not available for default Zope ACL)
    * Viewed pages
    * Added content
    * Created content
    * Modified content
    * Copied content
    * Moved content
    * Deleted content
    * Raised errors

