from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from api.UploadController import UploadController

router = APIRouter(prefix="/v1", tags=["upload"])


@router.post("/upload/", summary="upload files")
async def _(file: UploadFile = File(...),
            title=Form(...),
            description=Form(...)):
    # 读取文件内容
    f = UploadController()
    file = await f.upload_files(file=file,
                                description=description,
                                title=title)
    res = await f.send_files_to_git(title=file["title"], description=file["description"], file_content=file["file_content"], file_extension=file["file_extension"])
    return res
