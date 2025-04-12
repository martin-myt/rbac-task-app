from functools import wraps
from typing import Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from jose.exceptions import JWTError

from app.core.config import settings

security = HTTPBearer()


def get_token_auth_header(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    if credentials.scheme != "Bearer":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication scheme"
        )
    return credentials.credentials


def get_current_user(token: str = Depends(get_token_auth_header)) -> dict:
    try:
        unverified_claims = jwt.get_unverified_claims(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    try:
        payload = jwt.decode(
            token,
            settings.AUTH0_API_AUDIENCE,
            algorithms=settings.AUTH0_ALGORITHMS,
            issuer=settings.AUTH0_ISSUER
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )
    
    return payload


def require_role(role: str):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_user = kwargs.get("current_user")
            if not current_user or role not in current_user.get("roles", []):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"User does not have the required role: {role}"
                )
            return await func(*args, **kwargs)
        return wrapper
    return decorator 