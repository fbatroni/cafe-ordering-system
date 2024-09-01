from typing import Optional
from fastapi import Request
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.core.config import settings
from fastapi.security import HTTPBearer


class AuthenticationError(Exception):
    pass

# read this for more information on Authorization Headers
# https://medium.com/@london.lingo.01/building-secure-apis-with-http-authorization-header-tips-and-best-practices-2c56a5e4eb59

http_bearer = HTTPBearer()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, password_hash: str) -> bool:
    return pwd_context.verify(plain_password, password_hash)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({
        "exp": expire,
        "iss": settings.JWT_ISSUER  # Adding the issuer to the token payload
    })
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub") or None  # If "sub" is None, email will be None
        return email
    except JWTError:
        return None  # Return None if the token is invalid or decoding fails


def extract_token_from_header(authorization_header: str) -> str:
    """Extracts the token from the Authorization header."""
    if not authorization_header:
        raise AuthenticationError("Authorization header missing")

    parts = authorization_header.split()

    if parts[0].lower() != "bearer":
        raise AuthenticationError("Authorization header must start with Bearer")
    elif len(parts) == 1:
        raise AuthenticationError("Token not found")
    elif len(parts) > 2:
        raise AuthenticationError("Authorization header must be Bearer token")

    return parts[1]
