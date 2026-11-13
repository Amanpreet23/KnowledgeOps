from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError
import os
from datetime import datetime, timedelta, timezone
import jwt

_hasher = PasswordHasher()
SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_DAYS= int(os.getenv("JWT_EXPIRE_DAYS", "7"))


def hash_password(password:str) -> str:
    return _hasher.hash(password)


def verify_password(password:str, hashed_password:str) -> bool:
    try:
        return _hasher.verify(password, hashed_password)
    except (VerificationError, InvalidHashError):
        return False


def create_access_token(user_id, role: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "role": role,
        "type": "access",
        "iat": now,
        "exp": now + timedelta(days=JWT_EXPIRE_DAYS),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(token: str) -> str | None:
    """Return the user id from a valid access token, otherwise None."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except jwt.PyJWTError:
        return None
    if payload.get("type") != "access":
        return None
    return payload.get("sub")