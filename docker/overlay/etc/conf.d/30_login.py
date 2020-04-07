PROXYIDP_CONFIG = dict(
    base_url=os.getenv('PROXYIDP_URL', 'https://login.cesnet.cz/oidc/'),
    consumer_key=os.getenv('PROXYIDP_KEY', 'changeME!'),
    consumer_secret=os.getenv('PROXYIDP_SECRET', 'changeME!!'),
    authorize_url=os.getenv('PROXYIDP_AUTHORIZE_URL', 'https://login.cesnet.cz/oidc/authorize'),
    request_token_params={
        'scope': 'openid email profile eduPersonEntitlement'
    }
)

from invenio_cesnet_proxyidp.remote import PerunAuthRemote

OAUTHCLIENT_REMOTE_APPS = dict(
    proxyidp=PerunAuthRemote().remote_app(),
)

INVENIO_OAREPO_UI_LOGIN_URL = '/openid/login/proxyidp'

#: Extend Registration Form with username/displaynames
USERPROFILES_EXTEND_SECURITY_FORMS = True
