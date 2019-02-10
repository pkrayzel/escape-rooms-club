import json
import logging
from botocore.vendored import requests
import boto3
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('s3')


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

    logger.info(f'calling site url: {event["site_url"]}')
    response = requests.get(event["site_url"])

    try:
        response.raise_for_status()

        date_string = datetime.now().strftime('%Y/%m/%d/%H/%M')
        s3_key = f'{event["target_directory"]}/{date_string}/site.html'

        logger.info(f'Uploading file content to the bucket: {event["target_bucket"]} to the path: {s3_key}')
        client.put_object(Body=response.content, Bucket=event["target_bucket"], Key=s3_key)

    except Exception as e:
        logger.error(f'Something went wrong: {e}')
        return {
            'statusCode': 500,
            'error': e
        }

    return {
        'statusCode': 200,
        'body': "Success"
    }
