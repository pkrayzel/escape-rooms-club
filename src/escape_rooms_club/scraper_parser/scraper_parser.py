import boto3
import logging
from bs4 import BeautifulSoup

import exit_games


logger = logging.getLogger()
logger.setLevel(logging.INFO)

client = boto3.client('s3')

PARSER_PREFIX_EXIT_GAMES_CZ = 'exitgames.cz'

PARSERS = {
    PARSER_PREFIX_EXIT_GAMES_CZ: exit_games
}


def lambda_handler(event, context):
    """
    Lambda is invoked from s3 put event.
    {
        'Records':
            [
                {
                    'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'eu-west-1',
                    'eventTime': '2019-02-10T10:07:44.996Z',
                    'eventName': 'ObjectCreated:Put',
                    'userIdentity': {'principalId': 'AWS:AROAJOLQNCLWJZWXHSTJA:site-downloader'},
                    'requestParameters': {'sourceIPAddress': '34.240.203.234'},
                    'responseElements': {'x-amz-request-id': '7A3B4600A9DF6132',
                                         'x-amz-id-2': 'JpshiTjZ/VDWDDmjlbqkxJDRu1QKM7BpHK30Of4dfi9JG+fiNk9XCisZBMBkCc8mmEJwDAv9ILg='},
                    's3': {
                        's3SchemaVersion': '1.0', 'configurationId': 'exitgamescz-uploaded',
                        'bucket': {
                            'name': 'scrapers-sites',
                            'ownerIdentity': {'principalId': 'A61JXPXP2LQPN'},
                            'arn': 'arn:aws:s3:::scrapers-sites'},
                        'object': {
                            'key': 'exitgames.cz/2019/02/10/10/07/site.html', 'size': 93326,
                            'eTag': '7a6d6b2cedf6ca498725f0d341cea3b8', 'sequencer': '005C5FF7F0EA589AA6'
                        }
                    }
                }
            ]
    }
    :param event:
    :param context:
    :return:
    """
    logger.info(f"Received event: {event}")

    if 'Records' not in event:
        return {
            'statusCode': 400,
            'error': "Wrong input",
        }

    for record in event['Records']:
        s3_item = record['s3']

        bucket_name = s3_item['bucket']['name']
        key = s3_item['object']['key']

        # get the root directory of file
        parser_key = key.split('/')[0]

        if parser_key in PARSERS:
            obj = client.get_object(Bucket=bucket_name,
                                    Key=key)

            file_content = obj['Body'].read().decode('utf-8')
            parser = PARSERS[parser_key]

            logger.info(f"The file content with length {len(file_content)} will be parsed with parser: {parser}")

            soup = BeautifulSoup(file_content, 'html.parser')
            escape_rooms = parser.parse_all(soup)

            logger.info(f"Number of parsed escape rooms: {len(escape_rooms)}")

            for item in escape_rooms:
                logger.info(item)

        else:
            logger.error(f"Parsing site {parser_key} is not supported. Please add new parser for this site.")
            return {
                'statusCode': 400,
                'body': f"Parser {parser_key} not supported for file {key}."
            }

    return {
        'statusCode': 200,
        'body': "Success"
    }
