from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
from rest_frameword.authtoken.models import Token
class TokenAuthentication(BaseTokenAuth):
    keyword = 'Bearer'