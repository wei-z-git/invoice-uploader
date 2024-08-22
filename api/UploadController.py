from core.Response import success, fail
from configs.config import settings
from fastapi import File, UploadFile, Form
import httpx
import os
import json,base64


class UploadController:
    def __init__(self):
        self.endpoint = "gitee.com"
        self.owner = "amadeus666"
        self.repo = "Invoice"
        self.path_prefix = "ToBeOrganized/"
        self.access_token = "4fef6165fcdd31f45da7ea514a3aa924"

    async def upload_files(self, file: UploadFile = File(...),
                           title: str = Form(...),
                           description: str = Form(...)
                           ) -> dict:
        """
        """
        file_content = await file.read()
        file_content_encoded = base64.b64encode(file_content).decode()
        filename,file_extension = os.path.splitext(file.filename)
        return {
            "title": title,
            "description": description,
            "file_extension": file_extension,
            "file_content": file_content_encoded
        }

    async def send_files_to_git(self, title, description, file_content,file_extension):
        path = self.path_prefix+title+file_extension

        payload_dict = {
            'access_token': self.access_token,
            'content': file_content,
            'message': description
        }
        response = httpx.post(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=path), data=payload_dict)
        if response.status_code != 200:
            res=fail(msg="Upload failed!")
        else:
            res=success("ok",msg="Get env var successfully!")
        
        return res
