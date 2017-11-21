#!/usr/bin/env python
import sys
import os
import eventlet
from eventlet import wsgi
from paste.deploy import loadapp


class AnimalApplication(object):
	def __init__(self):
		print("-----AnimalApplication init")
		pass

	def __call__(self, environ, start_response):
		print("-------------AnimalApplication call-------------")
		start_response('200 OK', [('Content-Type', 'text/plain')])
		return ['This is a animal applicaltion for load by paste.deploy !\r\n']

	@classmethod
	def factory(cls, global_conf, **kwargs):
		return cls()


if '__main__' == __name__:

	print("-----animal app start-----------")
	configfile="animal.ini"
	application = loadapp("config:%s" % os.path.abspath(configfile), "animal")
	server = eventlet.spawn(wsgi.server,eventlet.listen(('', 8090)), application)
	server.wait()