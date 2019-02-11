import json
import logging
from datetime import datetime

from dao import WebClient, StorageClient
from domain import SiteDownloader

logger = logging.getLogger()
logger.setLevel(logging.INFO)


web_client = WebClient()
storage_client = StorageClient()
site_downloader = SiteDownloader(web_client, storage_client)


def handler(event, context):
    """
    event.site_url              - url of the site we want to download
    event.target_bucket         - name of the bucket to store data in
    event.target_directory      - name of the directory in the bucket to store data in
    :param event:
    :param context:
    :return:
    """
    logger.info(f'AWS Lambda - site downloader got event: {event}')

    success, error_message = site_downloader.download_site_and_store_its_content(
        site_url=event["site_url"],
        bucket_name=event["target_bucket"],
        target_directory=event["target_directory"]
    )

    if not success:
        return {
            'statusCode': 500,
            'error': error_message
        }

    return {
        'statusCode': 200,
        'body': "Success"
    }
