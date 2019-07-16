from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)
from .app import app, api
from tim.web.controllers import obj_a