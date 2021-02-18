from os import environ

# Oauth2 details
OAUTH_BASE_URI = environ["OAUTH_BASE_URI"]
OAUTH_PROXY = environ["OAUTH_PROXY"]
SERVICE_NAME = OAUTH_PROXY.replace('oauth2', 'identity-service')

TOKEN_URL = f"{OAUTH_BASE_URI}/{OAUTH_PROXY}/token"

# Test API (Hello World)
HELLO_WORLD_API_URL = environ.get("HELLO_WORLD_API_URL", None)
