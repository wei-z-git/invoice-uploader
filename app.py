
import os
from fastapi import FastAPI, HTTPException
from fastapi.exceptions import RequestValidationError
from core.Router import AllRouter
from fastapi_offline import FastAPIOffline
from configs.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPIOffline(
    version='0.0.1',
    title='RuntimeOpenapiPlatform'
    )


# 配置允许的源
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # 允许的源
    allow_credentials=True,
    allow_methods=["*"],  # 允许的HTTP方法
    allow_headers=["*"],  # 允许的HTTP头
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

