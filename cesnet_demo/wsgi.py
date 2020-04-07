from invenio_app.wsgi_rest import application
from oarepo_heartbeat.views import readiness, liveliness
#from oarepo_wsgi_rest import application
from invenio_app.wsgi_rest import application

class Middleware:
    """
    HeartBeat enabled WSGI middleware
    """

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        import pprint
        pprint.pprint(dict(environ))
        pprint.pprint(application.url_map)
        return self.app(environ, start_response)


application.wsgi_app = Middleware(application.wsgi_app)
