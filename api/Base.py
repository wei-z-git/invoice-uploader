from fastapi import APIRouter,Query
from api.UploadController import K8sController
from typing import Optional

router = APIRouter(prefix="/om/v1", tags=["O&M API Routes"])

@router.get("/k8s/env/get",summary="get k8s environment variable")
async def get_environment_variable(namespace: Optional[str] = Query("rt-cn", description="Namespace to get environment variable for"),pod_name: Optional[str] = Query("runtime-test-service-deployment-5c8b585bbf-crf58", description="Pod name to get environment variable for")):
    k=K8sController()
    return await k.get_environment_variable(namespace,pod_name)