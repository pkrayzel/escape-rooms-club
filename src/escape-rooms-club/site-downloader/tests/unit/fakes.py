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
            file_key: file_content
        }
    
    def find_all_file_keys_in_directory(self, bucket_name, directory):
        logger.info(f'Listing all file keys in directory {directory} in the bucket: {bucket_name}')

        if bucket_name not in self.files:
            return []

        return [key for key in self.files[bucket_name].keys() if key.startswith(directory)]

    def get(self, bucket_name, file_key):
        logger.info(f'Downloading file content for the file: {file_key} from the bucket: {bucket_name}')
        
        if bucket_name in self.files and file_key in self.files[bucket_name]:
            return self.files[bucket_name][file_key]

        logger.error(f'File not found in fake bucket!')
        return None     


class FakeWebClientBroken:

    def get(self, site_url):
        raise Exception(f"Request to a site_url: {site_url} has failed")


class FakeStorageClientBroken:
    
    def upload(self, bucket_name, file_key, file_content):
        raise Exception(f"Request to a file upload has failed")