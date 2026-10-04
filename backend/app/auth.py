import os
import uuid
from typing import Optional
import httpx
from fastapi import Depends , Request
from sqlalchemy.ext.asyncio import AsyncSession

from httpx_oauth.clients.google import GoogleOAuth2
from fastapi_users import BaseUserManager , FastAPIUsers , UUIDIDMixin
from fastapi_users.authentication import AuthenticationBackend, BearerTransport, JWTStrategy

from fastapi_users.db import SQLAlchemyUserDatabase

from app.database import get_async_session
from app.model import User ,OauthAccount

SECRET= os.getenv("SECRET_KEY")

google_oauth_client = GoogleOAuth2(
    os.getenv("GOOGLE_CLIENT_ID"),
    os.getenv("GOOGLE_CLIENT_SECRET")
)


async def get_user_db(session: AsyncSession=Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session,User, OauthAccount)


async def _fetch_google_picture(access_token: str) -> str | None:
    """httpx_oauth's GoogleOAuth2.get_id_email only requests/returns email —
    the profile photo isn't available anywhere in the standard fastapi-users
    OAuth flow, so this hits Google's own userinfo endpoint directly with
    the access token fastapi-users already obtained. Never raises — a
    failure here (network hiccup, Google API change) should never break
    login, it should just mean no avatar this time.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                "https://www.googleapis.com/oauth2/v3/userinfo",
                headers={"Authorization": f"Bearer {access_token}"},
            )
            response.raise_for_status()
            return response.json().get("picture")
    except httpx.HTTPError:
        return None


class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def oauth_callback(
        self,
        oauth_name: str,
        access_token: str,
        account_id: str,
        account_email: str,
        expires_at: int | None = None,
        refresh_token: str | None = None,
        request: Optional[Request] = None,
        *,
        associate_by_email: bool = False,
        is_verified_by_default: bool = False,
    ) -> User:
        user = await super().oauth_callback(
            oauth_name,
            access_token,
            account_id,
            account_email,
            expires_at,
            refresh_token,
            request,
            associate_by_email=associate_by_email,
            is_verified_by_default=is_verified_by_default,
        )

        # Only fetched once — if the user later changes their Google avatar,
        # we keep showing the old one rather than calling Google on every
        # single login just to re-check.
        if oauth_name == "google" and not user.picture:
            picture = await _fetch_google_picture(access_token)
            if picture:
                user = await self.user_db.update(user, {"picture": picture})

        return user

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

async def get_user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

def get_jwt_strategy() -> JWTStrategy:
    # 30 days. This is a single-token stopgap, not real refresh-token
    # rotation (no separate short-lived access token + long-lived refresh
    # token here) — see the 401 handling in AuthContext.jsx for what makes
    # an eventual expiry non-jarring regardless of this value.
    return JWTStrategy(secret=SECRET, lifetime_seconds=60 * 60 * 24 * 30)

auth_backend = AuthenticationBackend(
        name="jwt",
        transport=bearer_transport,
        get_strategy=get_jwt_strategy,
)
fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
current_active_user = fastapi_users.current_user(active=True)