from application.settings.base import *  # noqa


try:
    from application.settings.local import *  # noqa
except ImportError:
    pass
