import hug
from hug.middleware import CORSMiddleware

api = hug.API(__name__)
# allow_origins à restreindre pour le déploiement
api.http.add_middleware(CORSMiddleware(api, allow_origins=['*']))


@hug.get('/test')
def happy_birthday():
    """Basic test"""
    return "Succes"
