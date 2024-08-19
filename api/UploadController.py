from core.Response import success, fail
from configs.config import settings
from fastapi import File, UploadFile, Form
import httpx,json

class UploadController:
    def __init__(self):
        self.subscription_id = 'd07c204e-68de-4e1f-83f6-7cfa5f6afc0d'
        
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
            "title": title
        }
    async  def send_files_to_git(self, files,description):
        # get Blob SHA of the file
        sha = json.loads(httpx.get(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}?access_token={access_token}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path, access_token=self.access_token)).text)['sha']


        payload_dict = {
            'access_token': self.access_token,
            'content': files,
            'sha': sha,
            'message': description
        }
        response = httpx.put(
            "https://{endpoint}/api/v5/repos/{owner}/{repo}/contents/{path}".format(endpoint=self.endpoint, owner=self.owner, repo=self.repo, path=self.path), data=payload_dict).text
        print (response)
        return response