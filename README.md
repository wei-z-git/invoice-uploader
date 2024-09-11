# invoice-uploader

## Quick start

Python >= 3.12.4

### Install requirement

```
pip install --no-cache-dir --upgrade -r requirements.txt
```

### Start the server

```
uvicorn app:app --host 0.0.0.0 --port 80
```

### Invoice store

The gitee is used to store files, you need to change the fields with your own settings (api/UploadController.py)

```
        self.endpoint = "gitee.com"
        self.owner = "amadeus666"
        self.repo = "Invoice"
        self.path_prefix = "ToBeOrganized/"
        self.access_token = settings.GITEE_ACCESS_TOKEN
```
