from core.Response import success, fail
from configs.config import settings
from fastapi import File, UploadFile, Form
import httpx
import os
import base64


class UploadController:
    def __init__(self):
        self.endpoint = "gitee.com"
        self.owner = "amadeus666"
        self.repo = "Invoice"
        self.path_prefix = "ToBeOrganized/"
        self.access_token = settings.GITEE_ACCESS_TOKEN

    async def upload_files(self, file: UploadFile = File(...),
                           invoicetype: str = Form(...),
                           title: str = Form(...)
                           ) -> dict:
        """
        """
        file_content = await file.read()
        file_content_encoded = base64.b64encode(file_content).decode()
        filename,file_extension = os.path.splitext(file.filename)
        return {
            "invoicetype": invoicetype,
            "title": title,
            "file_extension": file_extension,
            "file_content": file_content_encoded
        }

    async def send_files_to_git(self, invoicetype, title, file_content,file_extension):
        path = self.path_prefix+invoicetype+title+file_extension

        payload_dict = {
            'access_token': self.access_token,
            'content': file_content,
            'message': title
        }
        try:
            response = httpx.post(
                "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=path), data=payload_dict)
            if 200 <= response.status_code < 300:
                res=success("ok",msg="Upload done!")
            else:
                res=fail(msg="Upload failed!")
        except Exception as e:
            res = fail(msg=f"An error occurred: {e}")
        
        return res
