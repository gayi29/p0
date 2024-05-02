import time
import jwt

secret_jwt = "84a2c7dee7766e99779bac74cf2f8cc4cba90c3a4847c1866c72306bb28432eaa0c68f1ddbca8e622d0686398f7f7764f7761a56004e7cf4afa7c3540371add7"
def create_token(token:str):
    return {"access token" : token}

def encode_jwt(email:str, password:str):
    D = {"email": email, "password": password, "exp": time.time() + (5*60)} # 5 min expiration time
    token =  jwt.encode(D, secret_jwt, algorithm = "HS256")
    return create_token(token)

def decode_jwt(token:str):
    try:
        decoding = jwt.decode(token, secret_jwt, algorithm ="HS256")
        if time.time() <= decoding['exp']:
            return decoding
        else:
            return "Token is Expired!"
    except:
        return {}
