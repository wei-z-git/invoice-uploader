
import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from core.Router import AllRouter
from fastapi_offline import FastAPIOffline
from configs.config import settings

app = FastAPIOffline(
    version='0.0.1',
    title='RuntimeOpenapiPlatform',
    root_path=settings.ROOT_PATH
    )

# app.root_path = "/api"
# app.add_event_handler("startup", startup(app))
# app.add_event_handler("shutdown", stopping(app))


# # Exception handler
# app.add_exception_handler(HTTPException, http_error_handler)
# app.add_exception_handler(RequestValidationError, http422_error_handler)
# app.add_exception_handler(UnicornException, unicorn_exception_handler)

# Register routes
app.include_router(AllRouter)

