# use the python virtual env that we set up in our domain's directory
import sys, os
INTERP = "/home/flskusr/scn2app.swiftcodeninja.com/env/bin/python"
if sys.executable != INTERP: os.execl(INTERP, INTERP, *sys.argv)

# use python's build in library to generate the WSGI response
def application(environ, start_response):
    start_response('200 OK', [('content-type', 'text/plain')])
    return ["Hello my pretty... " + sys.executable]

