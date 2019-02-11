from datetime import datetime

import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class SiteDownloader:

    def __init__(self, web_client, storage_client):
        self.web_client = web_client
        self.storage_client = storage_client

    def download_site_and_store_its_content(self, site_url, bucket_name, target_directory):
        """
            site_url              - url of the site we want to download
            bucket_name         - name of the bucket to store data in
            target_directory      - name of the directory in the bucket to store data in
        """
        logger.info(f'Trying to download site content from url: {site_url}')
        try:
            content = self.web_client.get(site_url)

            date_string = datetime.now().strftime('%Y/%m/%d/%H/%M')
            file_key = f'{target_directory}/{date_string}/site.html'

            self.storage_client.upload(
                bucket_name=bucket_name,
                file_key=file_key,
                file_content=content)

        except Exception as e:
            logger.error(f'Something went wrong: {e}')
            return False, e

        return True, None