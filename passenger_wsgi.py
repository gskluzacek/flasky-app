# instead of setting the python interpreter via os.execl(), use .htacces and the PassengerPython directive
# import sys, os
# INTERP = "/home/xxxx/xxxx/env/bin/python"
# if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

# uses Flask to implement the WSGI response
from manage import app as application
