from core.Response import success, fail
from configs.config import settings
from fastapi import File, UploadFile, Form
import httpx,json

class UploadController:
    def __init__(self):
        self.endpoint = "gitee.com"
        self.owner = "amadeus666"
        self.repo="Invoice"
        self.path_prefix="ToBeOrganized/"
        self.access_token="4fef6165fcdd31f45da7ea514a3aa924"

        
    async def upload_files(self,file: UploadFile = File(...),
                       description: str = Form(...),
                       title: str = Form(...)) -> dict:
        """
        """
        file_content = await file.read()

        # 构造响应
        return {
            "filename": file.filename,
            "content_type": file.content_type,
            "description": description,
            "title": title,
            "file_content":file_content
        }
    async  def send_files_to_git(self, title,description,file_content):
        path=self.path_prefix+title


        payload_dict = {
            'access_token': self.access_token,
            'content': file_content,
            'message': description
        }
        
        response = httpx.post(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=path), data=payload_dict).text
        print (response)
        return response