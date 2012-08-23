import os
import sys

apache_configuration= os.path.dirname(__file__) 
project = os.path.dirname(apache_configuration) 
workspace = os.path.dirname(project) 
sys.path.append(workspace) 

sys.path.append('/var/www/CSUBG')
sys.path.append('/var/www')
sys.path.append('/usr/lib/python2.6/dist-packages/django/')

import django.core.handlers.wsgi
import site



os.environ['DJANGO_SETTINGS_MODULE'] = 'CSUBG.settings'

application = django.core.handlers.wsgi.WSGIHandler()
