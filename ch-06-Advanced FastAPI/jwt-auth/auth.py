# /home/naman/Downloads/MyCode/CX---FastAPI-for-ML/ch-06-Advanced FastAPI/jwt-auth/auth.py
# Provides helpers to create and verify JWT access tokens.
# Exists to centralize token logic for authentication in the app.
# RELEVANT FILES: main.py, users.py

"""
Simple JWT helper utilities.

This module contains two small helper functions:
- create_access_token: build a signed JWT for a user.
- verify_token: decode and validate a JWT and return the subject (username).

Notes:
- Keep secrets out of source control in real projects. Use environment variables.
- The token expiry uses UTC-aware datetimes.
"""

from datetime import datetime, timedelta, timezone
from authlib.jose import JoseError, jwt
from fastapi import HTTPException

# constants
# In production, load SECRET_KEY from environment or a secret manager.
SECRET_KEY = 'my_secret'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRY_MINUTES = 30


def create_access_token(data: dict) -> str:
    """
    Create a signed JWT access token.

    Parameters:
    - data: a dict of claims to include in the token payload.
      Common claims: 'sub' (subject / username), 'roles', etc.

    Returns:
    - A JWT as a string.

    What the function does, step by step:
    1) Build a simple header that states the algorithm.
    2) Compute an expiry time (UTC). We add ACCESS_TOKEN_EXPIRY_MINUTES to now.
    3) Copy and extend the payload with the 'exp' claim.
    4) Encode (sign) the JWT using authlib. The result may be bytes,
       so we decode to UTF-8 text before returning.

    Important:
    - The 'exp' claim must be a datetime compatible with the JWT library.
    - We use timezone-aware UTC datetimes to avoid timezone bugs.
    """
    # JWT header telling which algorithm we used.
    header = {'alg': ALGORITHM}

    # Compute expiry in minutes. Use named argument to avoid passing days by mistake.
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)

    # Copy incoming data to avoid mutating caller's dict.
    payload = data.copy()

    # The standard JWT claim for expiry is 'exp'.
    payload.update({'exp': expire})

    # Encode/sign the token. authlib's encode may return bytes, so decode to str.
    token = jwt.encode(header, payload, SECRET_KEY)
    # token can be bytes or str depending on library version. Normalize to str.
    if isinstance(token, bytes):
        return token.decode('utf-8')
    return str(token)


def verify_token(token: str) -> str:
    """
    Verify and decode a JWT, returning the username (subject).

    Parameters:
    - token: the JWT string to verify.

    Returns:
    - The value of the 'sub' claim (commonly the username).

    Raises:
    - HTTPException(status_code=401) if the token is invalid,
      expired, or if the 'sub' claim is missing.

    What the function does:
    1) Decode the token using the SECRET_KEY.
    2) Call claims.validate() to check standard claims like 'exp'.
    3) Extract the 'sub' claim and return it.
    """
    try:
        # Decode and verify signature. This returns a claims-like object.
        claims = jwt.decode(token, SECRET_KEY)

        # Validate standard claims like expiration ('exp').
        claims.validate()

        # Extract the subject (username). Return it if present.
        username = claims.get('sub')
        if username is None:
            # Missing 'sub' claim - treat as unauthorized.
            raise HTTPException(status_code=401, detail='Token missing')

        return username
    except JoseError:
        # Any JOSE / JWT related error means the token is invalid.
        raise HTTPException(status_code=401, detail="Couldn't Validate Credentials")