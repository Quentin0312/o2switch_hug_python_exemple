import imp
import os
import sys
from hello import __hug_wsgi__

sys.path.insert(0, os.path.dirname(__file__))

application = __hug_wsgi__
