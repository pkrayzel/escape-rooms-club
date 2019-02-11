import boto3
from botocore.vendored import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class WebClient:

    def get(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content


class StorageClient:

    client = boto3.client('s3')

    def upload(self, bucket_name, file_key, file_content):
        logger.info(f'Uploading file content to the bucket: {bucket_name} to the path: {file_key}')
        response = self.client.put_object(
            Body=file_content,
            Bucket=bucket_name,
            Key=file_key
        )
        response.raise_for_status()

