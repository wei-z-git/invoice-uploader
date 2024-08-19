from fastapi import APIRouter, File, Form
from typing import Optional
from api.UploadController import UploadController

router = APIRouter(prefix="/v1", tags=["upload"])


@router.post("/upload/", summary="upload files")
async def _():
    # 读取文件内容
    f=UploadController()
    file=await f.upload_files(file=File(...),
                       description=Form(...),
                       title=Form(...))
    res=await f.send_files_to_git(file,file["description"])
    return res
