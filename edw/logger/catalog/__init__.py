import os
import json
import logging
import time
import inspect

from datetime import datetime

from Products.ZCatalog.ZCatalog import ZCatalog
from zope.globalrequest import getRequest

from edw.logger.util import get_user_data
from edw.logger.decorators import log_errors


logger = logging.getLogger("edw.logger")


EDW_LOGGER_CATALOG = os.environ.get(
    'EDW_LOGGER_CATALOG', 'true').lower() in ('true', 'yes', 'on')


EDW_LOGGER_CATALOG_STACK = os.environ.get(
    'EDW_LOGGER_CATALOG_STACK', 'false').lower() in ('true', 'yes', 'on')


old_catalog_object = ZCatalog.catalog_object


@log_errors("Cannot log catalog indexing")
def _log(catalog, obj, kwargs, dt):
    request = getRequest()

    url = request.URL
    action = getattr(url, 'split', lambda sep: [''])('/')[-1]
    user_data = get_user_data(request)

    idxs = kwargs.get('idxs', 'all')
    metadata = bool(kwargs.get('update_metadata', 1))

    stack = [
        '{}({}){}'.format(path, line, func)
        for _, path, line, func, _, _
        in inspect.stack()
    ] if EDW_LOGGER_CATALOG_STACK else ''

    logger.info(json.dumps({
        "IP": user_data['ip'],
        "User": user_data['user'],
        "Date": datetime.now().isoformat(),
        "URL": url,
        "Action": action,
        "Type": 'Catalog',
        "Catalog": catalog.absolute_url(1),
        "Object": '/'.join(obj.getPhysicalPath()),
        "Duration": dt,
        "Indexes": idxs,
        "Metadata": metadata,
        "Stack": stack,
        "LoggerName": logger.name,
    }))


def catalog_object(self, obj, *args, **kwargs):
    t_start = time.time()
    old_catalog_object(self, obj, *args, **kwargs)
    dt = time.time() - t_start
    _log(self, obj, kwargs, float('{0:.4f}'.format(dt)))


if EDW_LOGGER_CATALOG:
    ZCatalog.catalog_object = catalog_object
