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
* Added/created/copied/moved/deleted content - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_CONTENT** (e.g.: *EDW_LOGGER_CONTENT=false*);
* ZODB commits - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_DB** (e.g.: *EDW_LOGGER_DB=false*);
* Catalog indexing - Enabled by default. Can be disabled via environment variable **EDW_LOGGER_CATALOG** (e.g.: *EDW_LOGGER_CATALOG=false*);
* Catalog indexing stack trace - Disabled by default. Can be enabled via environment variable **EDW_LOGGER_CATALOG_STACK** (e.g.: *EDW_LOGGER_CATALOG_STACK=true*);


Privacy options
===============

User IP and user id are **disabled** by default, you can re-enable them using:

* **EDW_LOGGER_USER_IP** (e.g.: *EDW_LOGGER_USER_IP=true*);
* **EDW_LOGGER_USER_ID** (e.g.: *EDW_LOGGER_USER_ID=true*);

