'''
Combine all routers
'''
from api.Base import router
from fastapi import APIRouter

AllRouter = APIRouter()
# OM routers
AllRouter.include_router(router)

