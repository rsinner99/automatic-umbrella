import io
from minio import Minio

import settings

class Storage():
    name = 'default'
    client = Minio(
        endpoint=settings.MINIO_ENDPOINT,
        access_key=settings.MINIO_ACCESS_KEY,
        secret_key=settings.MINIO_SECRET_KEY,
        secure=settings.MINIO_SECURE
    )

    def __init__(self):
        found = self.client.bucket_exists(self.name)
        if not found:
            self.client.make_bucket(self.name)

    def list(self, prefix=None, include_version=False):
        objects = self.client.list_objects(self.name, prefix=prefix, include_version=include_version)
        return objects

    def get(self, object_name: str, version_id=None):
        try:
            response = self.client.get_object(self.name, object_name)
        finally:
            response.close()
            response.release_conn()
        try:
            content = response.data.decode('UTF-8')
        except:
            content = response.data
        return content

    def fget(self, object_name: str, file_path: str, version_id=None):
        return self.client.fget_object(self.name, object_name, file_path, version_id=version_id)

    def put(self, object_name:str, content: str, length: int):
        data = io.BytesIO(bytes(content, 'UTF-8'))
        result = self.client.put_object(
            self.name, object_name, data, len(content)
        )
        return result

    def fput(self, object_name: str, file_path: str):
        return self.client.fput_object(self.name, object_name, file_path)

    def remove(self, object_name, version_id=None):
        return self.client.remove_object(self.name, object_name, version_id=version_id)
