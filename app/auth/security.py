"""HTTP security boundary for the local NetShield console."""
from __future__ import annotations
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from app.auth.service import AuthService, COOKIE_NAME, CSRF_HEADER

PUBLIC_PATHS = {
    "/api/health", "/api/health/details", "/api/auth/login",
    "/api/auth/status", "/static/", "/favicon.ico"
}
MUTATING = {"POST", "PUT", "PATCH", "DELETE"}

class SecurityMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, auth: AuthService):
        super().__init__(app)
        self.auth = auth

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        if path.startswith("/api/") and not any(path == p or path.startswith(p) for p in PUBLIC_PATHS):
            current = self.auth.current_user(request.cookies.get(COOKIE_NAME))
            if not current:
                return JSONResponse({"error": "authentication_required"}, status_code=401)
            request.state.auth_user, request.state.csrf_hash = current
            if request.method in MUTATING and not self.auth.valid_csrf(
                request.headers.get(CSRF_HEADER), request.state.csrf_hash
            ):
                return JSONResponse({"error": "csrf_validation_failed"}, status_code=403)
        response = await call_next(request)
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Referrer-Policy"] = "same-origin"
        response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
        response.headers["Cache-Control"] = "no-store" if path.startswith("/api/auth") else response.headers.get("Cache-Control","")
        if request.url.path.startswith("/api/"):
            response.headers["Content-Security-Policy"] = "default-src 'none'; frame-ancestors 'none'"
        return response
