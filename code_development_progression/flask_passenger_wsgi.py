# use the python virtual env that we set up in our domain's directory
import sys, os
INTERP = "/home/flskusr/scn2app.swiftcodeninja.com/env/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

# hello uses Flask to implement the WSGI response
from hello import app as application

