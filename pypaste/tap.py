from wsgiref.simple_server import make_server
from paste import httpserver

class Tap(object):

    def __init__(self, in_arg):
        self.in_arg = in_arg
        print('-----------------start------------')
    def __call__(self, environ, start_response):
        status = '200 OK' # HTTP Status  
        headers = [('Content-type', 'text/plain; charset=utf-8')] # HTTP Headers  
        start_response(status, headers)  
  
        # The returned object is going to be printed  
        #return [b"Hello World"]
        body = '%s, %s!\n' % (self.in_arg, 'Tap')
        return [bytes(body, encoding = "utf8")  ]

def app_factory(global_config, in_arg):
    return Tap(in_arg)
