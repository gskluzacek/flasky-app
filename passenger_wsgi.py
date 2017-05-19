# instead of setting the python interpreter via os.execl(), use .htacces and the PassengerPython directive
# import sys, os
# INTERP = "/home/flskusr/scn2app.swiftcodeninja.com/env/bin/python"
# if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

# hello uses Flask to implement the WSGI response
from hello import app as application
