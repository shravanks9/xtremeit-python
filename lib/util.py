from datetime import datetime,timedelta
import jwt
import base64

JWT_Secret='npv6gg2JfUGGso28lMLI1kKdYMgqq99p'

def create_jwt(data:dict):
    d = datetime.utcnow() + timedelta(days=7)

    d = d.strftime('%s')
    data['exp'] = d

    encoded_jwt = jwt.encode(
        data, base64.b64decode(JWT_Secret), algorithm='HS256')
    return encoded_jwt