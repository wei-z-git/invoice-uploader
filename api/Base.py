from fastapi import APIRouter, UploadFile, File, Form
from typing import Optional
from api.UploadController import UploadController

router = APIRouter(prefix="/v1", tags=["upload"])


@router.post("/upload/", summary="upload files")
async def _(file: UploadFile = File(...),
            invoicetype=Form(...),
            title=Form(...)):
    # 读取文件内容
    f = UploadController()
    file = await f.upload_files(file=file,
                                title=title,
                                invoicetype=invoicetype)
    res = await f.send_files_to_git(invoicetype=file["invoicetype"], title=file["title"], file_content=file["file_content"], file_extension=file["file_extension"])
    return res
