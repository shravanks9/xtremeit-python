
import os
import jwt
import base64
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

auth = HTTPBearer(scheme_name='Bearer')

JWT_SECRET = 'npv6gg2JfUGGso28lMLI1kKdYMgqq99p'

# Verify token
def get_current_user(token: HTTPAuthorizationCredentials = Depends(auth)):

    credentials = token.credentials
    
    try:
        token_data = jwt.decode(credentials, base64.b64decode(JWT_SECRET), algorithms=['HS256'])

        return token_data

    except Exception as e:
        raise HTTPException(401, detail=str(e))