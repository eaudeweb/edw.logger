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

This package creates a new `edw.logger` log facility that logs to
INFO and ERROR the following events:

* Viewed pages - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_PUBLISHER** (e.g.: *EDW_LOGGER_PUBLISHER=false*;
* Raised errors - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_ERRORS** (e.g.: *EDW_LOGGER_ERRORS=false*);
* Added/created/copied/moved/deleted content - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_CONTENT** (e.g.: *EDW_LOGGER_CONTENT=false**);
* ZODB commits - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_DB** (e.g.: *EDW_LOGGER_DB=false**);
