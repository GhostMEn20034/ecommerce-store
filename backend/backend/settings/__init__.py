try:
    from .development import *
except ModuleNotFoundError:
    from .production import *
