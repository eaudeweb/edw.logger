import logging
import inspect
import json
from datetime import datetime
from zope.publisher.browser import BrowserView
from Products.PageTemplates.PageTemplate import PageTemplate
from edw.logger.util import get_ip


logger = logging.getLogger("edw.logger")


def traverse_wrapper(meth):
    """Extract some basic info about the object and view. traverse method
    gives us access to the traversed object"""

    def extract(self, *args, **kwargs):
        try:
            obj = meth(self, *args, **kwargs)
            try:
                if inspect.ismethod(obj):
                    return obj

                user = self.get('AUTHENTICATED_USER')
                username = user.getUserName()
                if username == 'Anonymous User':
                    partition = 'Anonymous'
                else:
                    partition = 'Authenticated'

                kv = {
                        'User': username,
                        'IP': get_ip(self),
                        'URL': self.URL,
                        'Partition': partition,
                        'Type': 'Traverse',
                        'Date': datetime.now().isoformat(),
                        }


                # Old school CMF style page template
                if isinstance(obj, PageTemplate):
                    kv['Action'] = obj.getId()
                    kv['Template'] = obj.pt_source_file()
                    parent = obj.getParentNode()
                    kv['Controller'] = parent.meta_type
                    kv['Object'] = parent.absolute_url()

                # Z3 style views
                elif isinstance(obj, BrowserView):
                    kv['Action'] = obj.__name__
                    if hasattr(obj.context, 'meta_type'):
                        kv['Controller'] = obj.context.meta_type
                    kv['Object'] = obj.context.absolute_url()

                if 'Controller' not in kv:
                    return obj

                logger.info(json.dumps(kv))
                return obj
            except:
                return obj

        except:
            raise

    return extract


from ZPublisher.BaseRequest import BaseRequest
BaseRequest.orig_traverse = BaseRequest.traverse
BaseRequest.traverse = traverse_wrapper(BaseRequest.orig_traverse)

