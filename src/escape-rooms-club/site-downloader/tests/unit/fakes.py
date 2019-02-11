import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class FakeWebClient:

    def __init__(self, site_map):
        self.site_map = site_map

    def get(self, site_url):
        if site_url in self.site_map:
            return self.site_map[site_url]
            
        return "<html>This is random content from the web</html>"


class FakeStorageClient:

    files = {}

    def upload(self, bucket_name, file_key, file_content):
        self.files[bucket_name] = {
            file_content: file_key
        }


class FakeWebClientBroken:

    def get(self, site_url):
        raise Exception(f"Request to a site_url: {site_url} has failed")


class FakeStorageClientBroken:
    
    def upload(self, bucket_name, file_key, file_content):
        raise Exception(f"Request to a file upload has failed")