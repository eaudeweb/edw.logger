import os
import json
import logging
from datetime import datetime

from Products.ZCatalog.ZCatalog import ZCatalog
from zope.globalrequest import getRequest

from edw.logger.util import get_user_data


EDW_LOGGER_CATALOG = os.environ.get(
    'EDW_LOGGER_CATALOG', 'true').lower() in ('true', 'yes', 'on')

logger = logging.getLogger("edw.logger")


old_catalog_object = ZCatalog.catalog_object


def _log(obj, idxs):
    print(obj, idxs)
    request = getRequest()

    url = request.URL
    action = getattr(url, 'split', lambda sep: [''])('/')[-1]
    user_data = get_user_data(request)

    logger.info(json.dumps({
        "IP": user_data['ip'],
        "User": user_data['user'],
        "Date": datetime.now().isoformat(),
        "URL": url,
        "Action": action,
        "Type": 'Catalog',
        "Indexes": idxs,
        "LoggerName": logger.name,
    }))


def catalog_object(*args, **kwargs):
    try:
        _log(args[1], kwargs.get('idxs', None))
    except Exception:
        pass
    return old_catalog_object(*args, **kwargs)


if EDW_LOGGER_CATALOG:
    ZCatalog.catalog_object = catalog_object
