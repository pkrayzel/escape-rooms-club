import boto3
import requests
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class WebClient:

    def get(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.content


class StorageClient:

    def __init__(self, endpoint_url=None):
        self.client = boto3.client('s3', endpoint_url=endpoint_url)

    def upload(self, bucket_name, file_key, file_content):
        logger.info(f'Uploading file content to the bucket: {bucket_name} to the path: {file_key}')
        self.client.put_object(
            Body=file_content,
            Bucket=bucket_name,
            Key=file_key
        )

    def find_all_file_keys_in_directory(self, bucket_name, directory):
        logger.info(f'Listing all file keys in directory {directory} in the bucket: {bucket_name}')
        response = self.client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=f'{directory}/' 
        )
        if response['KeyCount'] == 0:
            return []

        return [item['Key'] for item in response['Contents']]


    def get(self, bucket_name, file_key):
        logger.info(f'Downloading file content for the file: {file_key} from the bucket: {bucket_name}')
        response = self.client.get_object(
            Bucket=bucket_name,
            Key=file_key
        )
        return response['Body'].read()
