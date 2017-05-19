import sys, os

# use DreamHost's standard python

# use python's stand library to generate a WSGI response
def application(environ, start_response):
    start_response('200 OK', [('content-type', 'text/plain')])
    return ["Hello my pretty... " + sys.executable]

